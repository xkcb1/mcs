/*
 * Decompiled with CFR 0.2.0 (FabricMC d28b102d).
 */
package net.minecraft.server.command;

import com.google.common.collect.Lists;
import com.mojang.brigadier.ResultConsumer;
import com.mojang.brigadier.context.CommandContext;
import com.mojang.brigadier.exceptions.CommandSyntaxException;
import com.mojang.brigadier.exceptions.SimpleCommandExceptionType;
import com.mojang.brigadier.suggestion.Suggestions;
import com.mojang.brigadier.suggestion.SuggestionsBuilder;
import java.util.Collection;
import java.util.Objects;
import java.util.Set;
import java.util.concurrent.CompletableFuture;
import java.util.function.BinaryOperator;
import java.util.function.IntConsumer;
import java.util.function.Supplier;
import java.util.stream.Stream;
import net.minecraft.command.CommandSource;
import net.minecraft.command.argument.EntityAnchorArgumentType;
import net.minecraft.entity.Entity;
import net.minecraft.network.message.MessageType;
import net.minecraft.network.message.SentMessage;
import net.minecraft.network.message.SignedCommandArguments;
import net.minecraft.registry.DynamicRegistryManager;
import net.minecraft.registry.Registries;
import net.minecraft.registry.Registry;
import net.minecraft.registry.RegistryKey;
import net.minecraft.resource.featuretoggle.FeatureSet;
import net.minecraft.server.MinecraftServer;
import net.minecraft.server.command.CommandOutput;
import net.minecraft.server.network.ServerPlayerEntity;
import net.minecraft.server.world.ServerWorld;
import net.minecraft.sound.SoundEvent;
import net.minecraft.text.MutableText;
import net.minecraft.text.Text;
import net.minecraft.util.Formatting;
import net.minecraft.util.Identifier;
import net.minecraft.util.math.MathHelper;
import net.minecraft.util.math.Vec2f;
import net.minecraft.util.math.Vec3d;
import net.minecraft.util.thread.FutureQueue;
import net.minecraft.world.GameRules;
import net.minecraft.world.World;
import net.minecraft.world.dimension.DimensionType;
import org.jetbrains.annotations.Nullable;

/**
 * Represents a command source used on server side.
 * 
 * @see MinecraftServer#getCommandSource()
 * @see Entity#getCommandSource()
 */
public class ServerCommandSource
implements CommandSource {
    public static final SimpleCommandExceptionType REQUIRES_PLAYER_EXCEPTION = new SimpleCommandExceptionType(Text.translatable("permissions.requires.player"));
    public static final SimpleCommandExceptionType REQUIRES_ENTITY_EXCEPTION = new SimpleCommandExceptionType(Text.translatable("permissions.requires.entity"));
    private final CommandOutput output;
    private final Vec3d position;
    private final ServerWorld world;
    private final int level;
    private final String name;
    private final Text displayName;
    private final MinecraftServer server;
    private final boolean silent;
    @Nullable
    private final Entity entity;
    @Nullable
    private final ResultConsumer<ServerCommandSource> resultConsumer;
    private final EntityAnchorArgumentType.EntityAnchor entityAnchor;
    private final Vec2f rotation;
    private final SignedCommandArguments signedArguments;
    private final FutureQueue messageChainTaskQueue;
    private final IntConsumer returnValueConsumer;

    public ServerCommandSource(CommandOutput output, Vec3d pos, Vec2f rot, ServerWorld world, int level, String name, Text displayName, MinecraftServer server, @Nullable Entity entity) {
        this(output, pos, rot, world, level, name, displayName, server, entity, false, (context, success, result) -> {}, EntityAnchorArgumentType.EntityAnchor.FEET, SignedCommandArguments.EMPTY, FutureQueue.immediate(server), i -> {});
    }

    protected ServerCommandSource(CommandOutput output, Vec3d pos, Vec2f rot, ServerWorld world, int level, String name, Text displayName, MinecraftServer server, @Nullable Entity entity, boolean silent, @Nullable ResultConsumer<ServerCommandSource> consumer, EntityAnchorArgumentType.EntityAnchor entityAnchor, SignedCommandArguments signedArguments, FutureQueue messageChainTaskQueue, IntConsumer returnValueConsumer) {
        this.output = output;
        this.position = pos;
        this.world = world;
        this.silent = silent;
        this.entity = entity;
        this.level = level;
        this.name = name;
        this.displayName = displayName;
        this.server = server;
        this.resultConsumer = consumer;
        this.entityAnchor = entityAnchor;
        this.rotation = rot;
        this.signedArguments = signedArguments;
        this.messageChainTaskQueue = messageChainTaskQueue;
        this.returnValueConsumer = returnValueConsumer;
    }

    public ServerCommandSource withOutput(CommandOutput output) {
        if (this.output == output) {
            return this;
        }
        return new ServerCommandSource(output, this.position, this.rotation, this.world, this.level, this.name, this.displayName, this.server, this.entity, this.silent, this.resultConsumer, this.entityAnchor, this.signedArguments, this.messageChainTaskQueue, this.returnValueConsumer);
    }

    public ServerCommandSource withEntity(Entity entity) {
        if (this.entity == entity) {
            return this;
        }
        return new ServerCommandSource(this.output, this.position, this.rotation, this.world, this.level, entity.getName().getString(), entity.getDisplayName(), this.server, entity, this.silent, this.resultConsumer, this.entityAnchor, this.signedArguments, this.messageChainTaskQueue, this.returnValueConsumer);
    }

    public ServerCommandSource withPosition(Vec3d position) {
        if (this.position.equals(position)) {
            return this;
        }
        return new ServerCommandSource(this.output, position, this.rotation, this.world, this.level, this.name, this.displayName, this.server, this.entity, this.silent, this.resultConsumer, this.entityAnchor, this.signedArguments, this.messageChainTaskQueue, this.returnValueConsumer);
    }

    public ServerCommandSource withRotation(Vec2f rotation) {
        if (this.rotation.equals(rotation)) {
            return this;
        }
        return new ServerCommandSource(this.output, this.position, rotation, this.world, this.level, this.name, this.displayName, this.server, this.entity, this.silent, this.resultConsumer, this.entityAnchor, this.signedArguments, this.messageChainTaskQueue, this.returnValueConsumer);
    }

    public ServerCommandSource withConsumer(ResultConsumer<ServerCommandSource> consumer) {
        if (Objects.equals(this.resultConsumer, consumer)) {
            return this;
        }
        return new ServerCommandSource(this.output, this.position, this.rotation, this.world, this.level, this.name, this.displayName, this.server, this.entity, this.silent, consumer, this.entityAnchor, this.signedArguments, this.messageChainTaskQueue, this.returnValueConsumer);
    }

    public ServerCommandSource mergeConsumers(ResultConsumer<ServerCommandSource> consumer, BinaryOperator<ResultConsumer<ServerCommandSource>> merger) {
        ResultConsumer resultConsumer = (ResultConsumer)merger.apply(this.resultConsumer, consumer);
        return this.withConsumer(resultConsumer);
    }

    public ServerCommandSource withSilent() {
        if (this.silent || this.output.cannotBeSilenced()) {
            return this;
        }
        return new ServerCommandSource(this.output, this.position, this.rotation, this.world, this.level, this.name, this.displayName, this.server, this.entity, true, this.resultConsumer, this.entityAnchor, this.signedArguments, this.messageChainTaskQueue, this.returnValueConsumer);
    }

    public ServerCommandSource withLevel(int level) {
        if (level == this.level) {
            return this;
        }
        return new ServerCommandSource(this.output, this.position, this.rotation, this.world, level, this.name, this.displayName, this.server, this.entity, this.silent, this.resultConsumer, this.entityAnchor, this.signedArguments, this.messageChainTaskQueue, this.returnValueConsumer);
    }

    public ServerCommandSource withMaxLevel(int level) {
        if (level <= this.level) {
            return this;
        }
        return new ServerCommandSource(this.output, this.position, this.rotation, this.world, level, this.name, this.displayName, this.server, this.entity, this.silent, this.resultConsumer, this.entityAnchor, this.signedArguments, this.messageChainTaskQueue, this.returnValueConsumer);
    }

    public ServerCommandSource withEntityAnchor(EntityAnchorArgumentType.EntityAnchor anchor) {
        if (anchor == this.entityAnchor) {
            return this;
        }
        return new ServerCommandSource(this.output, this.position, this.rotation, this.world, this.level, this.name, this.displayName, this.server, this.entity, this.silent, this.resultConsumer, anchor, this.signedArguments, this.messageChainTaskQueue, this.returnValueConsumer);
    }

    public ServerCommandSource withWorld(ServerWorld world) {
        if (world == this.world) {
            return this;
        }
        double d = DimensionType.getCoordinateScaleFactor(this.world.getDimension(), world.getDimension());
        Vec3d vec3d = new Vec3d(this.position.x * d, this.position.y, this.position.z * d);
        return new ServerCommandSource(this.output, vec3d, this.rotation, world, this.level, this.name, this.displayName, this.server, this.entity, this.silent, this.resultConsumer, this.entityAnchor, this.signedArguments, this.messageChainTaskQueue, this.returnValueConsumer);
    }

    public ServerCommandSource withLookingAt(Entity entity, EntityAnchorArgumentType.EntityAnchor anchor) {
        return this.withLookingAt(anchor.positionAt(entity));
    }

    public ServerCommandSource withLookingAt(Vec3d position) {
        Vec3d vec3d = this.entityAnchor.positionAt(this);
        double d = position.x - vec3d.x;
        double e = position.y - vec3d.y;
        double f = position.z - vec3d.z;
        double g = Math.sqrt(d * d + f * f);
        float h = MathHelper.wrapDegrees((float)(-(MathHelper.atan2(e, g) * 57.2957763671875)));
        float i = MathHelper.wrapDegrees((float)(MathHelper.atan2(f, d) * 57.2957763671875) - 90.0f);
        return this.withRotation(new Vec2f(h, i));
    }

    public ServerCommandSource withSignedArguments(SignedCommandArguments signedArguments) {
        if (signedArguments == this.signedArguments) {
            return this;
        }
        return new ServerCommandSource(this.output, this.position, this.rotation, this.world, this.level, this.name, this.displayName, this.server, this.entity, this.silent, this.resultConsumer, this.entityAnchor, signedArguments, this.messageChainTaskQueue, this.returnValueConsumer);
    }

    public ServerCommandSource withMessageChainTaskQueue(FutureQueue messageChainTaskQueue) {
        if (messageChainTaskQueue == this.messageChainTaskQueue) {
            return this;
        }
        return new ServerCommandSource(this.output, this.position, this.rotation, this.world, this.level, this.name, this.displayName, this.server, this.entity, this.silent, this.resultConsumer, this.entityAnchor, this.signedArguments, messageChainTaskQueue, this.returnValueConsumer);
    }

    public ServerCommandSource withReturnValueConsumer(IntConsumer returnValueConsumer) {
        if (returnValueConsumer == this.returnValueConsumer) {
            return this;
        }
        return new ServerCommandSource(this.output, this.position, this.rotation, this.world, this.level, this.name, this.displayName, this.server, this.entity, this.silent, this.resultConsumer, this.entityAnchor, this.signedArguments, this.messageChainTaskQueue, returnValueConsumer);
    }

    public Text getDisplayName() {
        return this.displayName;
    }

    public String getName() {
        return this.name;
    }

    @Override
    public boolean hasPermissionLevel(int level) {
        return this.level >= level;
    }

    public Vec3d getPosition() {
        return this.position;
    }

    public ServerWorld getWorld() {
        return this.world;
    }

    /**
     * Gets the entity from this command source or returns null if this command source is not an entity.
     */
    @Nullable
    public Entity getEntity() {
        return this.entity;
    }

    /**
     * Gets the entity from this command source or throws a command syntax exception if this command source is not an entity.
     */
    public Entity getEntityOrThrow() throws CommandSyntaxException {
        if (this.entity == null) {
            throw REQUIRES_ENTITY_EXCEPTION.create();
        }
        return this.entity;
    }

    /**
     * {@return the player from this command source}
     * 
     * @throws CommandSyntaxException if this command source is not a player
     */
    public ServerPlayerEntity getPlayerOrThrow() throws CommandSyntaxException {
        Entity entity = this.entity;
        if (entity instanceof ServerPlayerEntity) {
            ServerPlayerEntity serverPlayerEntity = (ServerPlayerEntity)entity;
            return serverPlayerEntity;
        }
        throw REQUIRES_PLAYER_EXCEPTION.create();
    }

    /**
     * {@return the player from this command source, or {@code null} if the source is not a player}
     */
    @Nullable
    public ServerPlayerEntity getPlayer() {
        ServerPlayerEntity serverPlayerEntity;
        Entity entity = this.entity;
        return entity instanceof ServerPlayerEntity ? (serverPlayerEntity = (ServerPlayerEntity)entity) : null;
    }

    public boolean isExecutedByPlayer() {
        return this.entity instanceof ServerPlayerEntity;
    }

    public Vec2f getRotation() {
        return this.rotation;
    }

    public MinecraftServer getServer() {
        return this.server;
    }

    public EntityAnchorArgumentType.EntityAnchor getEntityAnchor() {
        return this.entityAnchor;
    }

    public SignedCommandArguments getSignedArguments() {
        return this.signedArguments;
    }

    public FutureQueue getMessageChainTaskQueue() {
        return this.messageChainTaskQueue;
    }

    public IntConsumer getReturnValueConsumer() {
        return this.returnValueConsumer;
    }

    /**
     * {@return whether to filter text sent to {@code recipient}}
     * 
     * <p>This returns {@code true} if either of the command executor or the recipient
     * requires text filtering, unless {@code recipient} executed the command, where
     * {@code false} is always returned.
     */
    public boolean shouldFilterText(ServerPlayerEntity recipient) {
        ServerPlayerEntity serverPlayerEntity = this.getPlayer();
        if (recipient == serverPlayerEntity) {
            return false;
        }
        return serverPlayerEntity != null && serverPlayerEntity.shouldFilterText() || recipient.shouldFilterText();
    }

    /**
     * Sends {@code message} as a chat message to the command's executor, or to the server's log
     * if the command is not executed by a player.
     */
    public void sendChatMessage(SentMessage message, boolean filterMaskEnabled, MessageType.Parameters params) {
        if (this.silent) {
            return;
        }
        ServerPlayerEntity serverPlayerEntity = this.getPlayer();
        if (serverPlayerEntity != null) {
            serverPlayerEntity.sendChatMessage(message, filterMaskEnabled, params);
        } else {
            this.output.sendMessage(params.applyChatDecoration(message.getContent()));
        }
    }

    /**
     * Sends {@code message} as the feedback to the command's executor, or to the server's log
     * if the command is not executed by a player.
     */
    public void sendMessage(Text message) {
        if (this.silent) {
            return;
        }
        ServerPlayerEntity serverPlayerEntity = this.getPlayer();
        if (serverPlayerEntity != null) {
            serverPlayerEntity.sendMessage(message);
        } else {
            this.output.sendMessage(message);
        }
    }

    public void sendFeedback(Supplier<Text> feedbackSupplier, boolean broadcastToOps) {
        boolean bl2;
        boolean bl = this.output.shouldReceiveFeedback() && !this.silent;
        boolean bl3 = bl2 = broadcastToOps && this.output.shouldBroadcastConsoleToOps() && !this.silent;
        if (!bl && !bl2) {
            return;
        }
        Text text = feedbackSupplier.get();
        if (bl) {
            this.output.sendMessage(text);
        }
        if (bl2) {
            this.sendToOps(text);
        }
    }

    private void sendToOps(Text message) {
        MutableText text = Text.translatable("chat.type.admin", this.getDisplayName(), message).formatted(Formatting.GRAY, Formatting.ITALIC);
        if (this.server.getGameRules().getBoolean(GameRules.SEND_COMMAND_FEEDBACK)) {
            for (ServerPlayerEntity serverPlayerEntity : this.server.getPlayerManager().getPlayerList()) {
                if (serverPlayerEntity == this.output || !this.server.getPlayerManager().isOperator(serverPlayerEntity.getGameProfile())) continue;
                serverPlayerEntity.sendMessage(text);
            }
        }
        if (this.output != this.server && this.server.getGameRules().getBoolean(GameRules.LOG_ADMIN_COMMANDS)) {
            this.server.sendMessage(text);
        }
    }

    public void sendError(Text message) {
        if (this.output.shouldTrackOutput() && !this.silent) {
            this.output.sendMessage(Text.empty().append(message).formatted(Formatting.RED));
        }
    }

    public void onCommandComplete(CommandContext<ServerCommandSource> context, boolean success, int result) {
        if (this.resultConsumer != null) {
            this.resultConsumer.onCommandComplete(context, success, result);
        }
    }

    @Override
    public Collection<String> getPlayerNames() {
        return Lists.newArrayList(this.server.getPlayerNames());
    }

    @Override
    public Collection<String> getTeamNames() {
        return this.server.getScoreboard().getTeamNames();
    }

    @Override
    public Stream<Identifier> getSoundIds() {
        return Registries.SOUND_EVENT.stream().map(SoundEvent::getId);
    }

    @Override
    public Stream<Identifier> getRecipeIds() {
        return this.server.getRecipeManager().keys();
    }

    @Override
    public CompletableFuture<Suggestions> getCompletions(CommandContext<?> context) {
        return Suggestions.empty();
    }

    @Override
    public CompletableFuture<Suggestions> listIdSuggestions(RegistryKey<? extends Registry<?>> registryRef, CommandSource.SuggestedIdType suggestedIdType, SuggestionsBuilder builder, CommandContext<?> context) {
        return this.getRegistryManager().getOptional(registryRef).map(registry -> {
            this.suggestIdentifiers((Registry<?>)registry, suggestedIdType, builder);
            return builder.buildFuture();
        }).orElseGet(Suggestions::empty);
    }

    @Override
    public Set<RegistryKey<World>> getWorldKeys() {
        return this.server.getWorldRegistryKeys();
    }

    @Override
    public DynamicRegistryManager getRegistryManager() {
        return this.server.getRegistryManager();
    }

    @Override
    public FeatureSet getEnabledFeatures() {
        return this.world.getEnabledFeatures();
    }
}

