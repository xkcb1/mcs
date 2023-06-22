/*
 * Decompiled with CFR 0.2.0 (FabricMC d28b102d).
 */
package net.minecraft.server.command;

import com.mojang.brigadier.CommandDispatcher;
import com.mojang.brigadier.arguments.FloatArgumentType;
import com.mojang.brigadier.builder.ArgumentBuilder;
import com.mojang.brigadier.builder.LiteralArgumentBuilder;
import com.mojang.brigadier.builder.RequiredArgumentBuilder;
import com.mojang.brigadier.exceptions.CommandSyntaxException;
import com.mojang.brigadier.exceptions.SimpleCommandExceptionType;
import java.util.Collection;
import net.minecraft.command.argument.EntityArgumentType;
import net.minecraft.command.argument.IdentifierArgumentType;
import net.minecraft.command.argument.Vec3ArgumentType;
import net.minecraft.command.suggestion.SuggestionProviders;
import net.minecraft.network.packet.s2c.play.PlaySoundS2CPacket;
import net.minecraft.registry.entry.RegistryEntry;
import net.minecraft.server.command.CommandManager;
import net.minecraft.server.command.ServerCommandSource;
import net.minecraft.server.network.ServerPlayerEntity;
import net.minecraft.sound.SoundCategory;
import net.minecraft.sound.SoundEvent;
import net.minecraft.text.Text;
import net.minecraft.util.Identifier;
import net.minecraft.util.math.MathHelper;
import net.minecraft.util.math.Vec3d;

public class PlaySoundCommand {
    private static final SimpleCommandExceptionType FAILED_EXCEPTION = new SimpleCommandExceptionType(Text.translatable("commands.playsound.failed"));

    public static void register(CommandDispatcher<ServerCommandSource> dispatcher) {
        RequiredArgumentBuilder<ServerCommandSource, Identifier> requiredArgumentBuilder = CommandManager.argument("sound", IdentifierArgumentType.identifier()).suggests(SuggestionProviders.AVAILABLE_SOUNDS);
        for (SoundCategory soundCategory : SoundCategory.values()) {
            requiredArgumentBuilder.then(PlaySoundCommand.makeArgumentsForCategory(soundCategory));
        }
        dispatcher.register((LiteralArgumentBuilder)((LiteralArgumentBuilder)CommandManager.literal("playsound").requires(source -> source.hasPermissionLevel(2))).then(requiredArgumentBuilder));
    }

    private static LiteralArgumentBuilder<ServerCommandSource> makeArgumentsForCategory(SoundCategory category) {
        return (LiteralArgumentBuilder)CommandManager.literal(category.getName()).then((ArgumentBuilder<ServerCommandSource, ?>)((RequiredArgumentBuilder)CommandManager.argument("targets", EntityArgumentType.players()).executes(context -> PlaySoundCommand.execute((ServerCommandSource)context.getSource(), EntityArgumentType.getPlayers(context, "targets"), IdentifierArgumentType.getIdentifier(context, "sound"), category, ((ServerCommandSource)context.getSource()).getPosition(), 1.0f, 1.0f, 0.0f))).then(((RequiredArgumentBuilder)CommandManager.argument("pos", Vec3ArgumentType.vec3()).executes(context -> PlaySoundCommand.execute((ServerCommandSource)context.getSource(), EntityArgumentType.getPlayers(context, "targets"), IdentifierArgumentType.getIdentifier(context, "sound"), category, Vec3ArgumentType.getVec3(context, "pos"), 1.0f, 1.0f, 0.0f))).then(((RequiredArgumentBuilder)CommandManager.argument("volume", FloatArgumentType.floatArg(0.0f)).executes(context -> PlaySoundCommand.execute((ServerCommandSource)context.getSource(), EntityArgumentType.getPlayers(context, "targets"), IdentifierArgumentType.getIdentifier(context, "sound"), category, Vec3ArgumentType.getVec3(context, "pos"), context.getArgument("volume", Float.class).floatValue(), 1.0f, 0.0f))).then(((RequiredArgumentBuilder)CommandManager.argument("pitch", FloatArgumentType.floatArg(0.0f, 2.0f)).executes(context -> PlaySoundCommand.execute((ServerCommandSource)context.getSource(), EntityArgumentType.getPlayers(context, "targets"), IdentifierArgumentType.getIdentifier(context, "sound"), category, Vec3ArgumentType.getVec3(context, "pos"), context.getArgument("volume", Float.class).floatValue(), context.getArgument("pitch", Float.class).floatValue(), 0.0f))).then(CommandManager.argument("minVolume", FloatArgumentType.floatArg(0.0f, 1.0f)).executes(context -> PlaySoundCommand.execute((ServerCommandSource)context.getSource(), EntityArgumentType.getPlayers(context, "targets"), IdentifierArgumentType.getIdentifier(context, "sound"), category, Vec3ArgumentType.getVec3(context, "pos"), context.getArgument("volume", Float.class).floatValue(), context.getArgument("pitch", Float.class).floatValue(), context.getArgument("minVolume", Float.class).floatValue())))))));
    }

    private static int execute(ServerCommandSource source, Collection<ServerPlayerEntity> targets, Identifier sound, SoundCategory category, Vec3d pos, float volume, float pitch, float minVolume) throws CommandSyntaxException {
        RegistryEntry<SoundEvent> registryEntry = RegistryEntry.of(SoundEvent.of(sound));
        double d = MathHelper.square(registryEntry.value().getDistanceToTravel(volume));
        int i = 0;
        long l = source.getWorld().getRandom().nextLong();
        for (ServerPlayerEntity serverPlayerEntity : targets) {
            double e = pos.x - serverPlayerEntity.getX();
            double f = pos.y - serverPlayerEntity.getY();
            double g = pos.z - serverPlayerEntity.getZ();
            double h = e * e + f * f + g * g;
            Vec3d vec3d = pos;
            float j = volume;
            if (h > d) {
                if (minVolume <= 0.0f) continue;
                double k = Math.sqrt(h);
                vec3d = new Vec3d(serverPlayerEntity.getX() + e / k * 2.0, serverPlayerEntity.getY() + f / k * 2.0, serverPlayerEntity.getZ() + g / k * 2.0);
                j = minVolume;
            }
            serverPlayerEntity.networkHandler.sendPacket(new PlaySoundS2CPacket(registryEntry, category, vec3d.getX(), vec3d.getY(), vec3d.getZ(), j, pitch, l));
            ++i;
        }
        if (i == 0) {
            throw FAILED_EXCEPTION.create();
        }
        if (targets.size() == 1) {
            source.sendFeedback(() -> Text.translatable("commands.playsound.success.single", sound, ((ServerPlayerEntity)targets.iterator().next()).getDisplayName()), true);
        } else {
            source.sendFeedback(() -> Text.translatable("commands.playsound.success.multiple", sound, targets.size()), true);
        }
        return i;
    }
}

