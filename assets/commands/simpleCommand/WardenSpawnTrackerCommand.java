/*
 * Decompiled with CFR 0.2.0 (FabricMC d28b102d).
 */
package net.minecraft.server.command;

import com.google.common.collect.ImmutableList;
import com.mojang.brigadier.CommandDispatcher;
import com.mojang.brigadier.arguments.IntegerArgumentType;
import com.mojang.brigadier.builder.ArgumentBuilder;
import com.mojang.brigadier.builder.LiteralArgumentBuilder;
import java.util.Collection;
import net.minecraft.block.entity.SculkShriekerWarningManager;
import net.minecraft.entity.player.PlayerEntity;
import net.minecraft.server.command.CommandManager;
import net.minecraft.server.command.ServerCommandSource;
import net.minecraft.text.Text;

public class WardenSpawnTrackerCommand {
    public static void register(CommandDispatcher<ServerCommandSource> dispatcher) {
        dispatcher.register((LiteralArgumentBuilder)((LiteralArgumentBuilder)((LiteralArgumentBuilder)CommandManager.literal("warden_spawn_tracker").requires(source -> source.hasPermissionLevel(2))).then(CommandManager.literal("clear").executes(context -> WardenSpawnTrackerCommand.clearTracker((ServerCommandSource)context.getSource(), ImmutableList.of(((ServerCommandSource)context.getSource()).getPlayerOrThrow()))))).then(CommandManager.literal("set").then((ArgumentBuilder<ServerCommandSource, ?>)CommandManager.argument("warning_level", IntegerArgumentType.integer(0, 4)).executes(context -> WardenSpawnTrackerCommand.setWarningLevel((ServerCommandSource)context.getSource(), ImmutableList.of(((ServerCommandSource)context.getSource()).getPlayerOrThrow()), IntegerArgumentType.getInteger(context, "warning_level"))))));
    }

    private static int setWarningLevel(ServerCommandSource source, Collection<? extends PlayerEntity> players, int warningCount) {
        for (PlayerEntity playerEntity : players) {
            playerEntity.getSculkShriekerWarningManager().ifPresent(warningManager -> warningManager.setWarningLevel(warningCount));
        }
        if (players.size() == 1) {
            source.sendFeedback(() -> Text.translatable("commands.warden_spawn_tracker.set.success.single", ((PlayerEntity)players.iterator().next()).getDisplayName()), true);
        } else {
            source.sendFeedback(() -> Text.translatable("commands.warden_spawn_tracker.set.success.multiple", players.size()), true);
        }
        return players.size();
    }

    private static int clearTracker(ServerCommandSource source, Collection<? extends PlayerEntity> players) {
        for (PlayerEntity playerEntity : players) {
            playerEntity.getSculkShriekerWarningManager().ifPresent(SculkShriekerWarningManager::reset);
        }
        if (players.size() == 1) {
            source.sendFeedback(() -> Text.translatable("commands.warden_spawn_tracker.clear.success.single", ((PlayerEntity)players.iterator().next()).getDisplayName()), true);
        } else {
            source.sendFeedback(() -> Text.translatable("commands.warden_spawn_tracker.clear.success.multiple", players.size()), true);
        }
        return players.size();
    }
}

