/*
 * Decompiled with CFR 0.2.0 (FabricMC d28b102d).
 */
package net.minecraft.server.command;

import com.google.common.collect.Lists;
import com.mojang.brigadier.CommandDispatcher;
import com.mojang.brigadier.arguments.IntegerArgumentType;
import com.mojang.brigadier.arguments.StringArgumentType;
import com.mojang.brigadier.builder.ArgumentBuilder;
import com.mojang.brigadier.builder.LiteralArgumentBuilder;
import com.mojang.brigadier.builder.RequiredArgumentBuilder;
import com.mojang.brigadier.exceptions.CommandSyntaxException;
import com.mojang.brigadier.exceptions.Dynamic2CommandExceptionType;
import com.mojang.brigadier.exceptions.SimpleCommandExceptionType;
import com.mojang.brigadier.suggestion.Suggestions;
import com.mojang.brigadier.suggestion.SuggestionsBuilder;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Map;
import java.util.concurrent.CompletableFuture;
import net.minecraft.command.CommandSource;
import net.minecraft.command.argument.OperationArgumentType;
import net.minecraft.command.argument.ScoreHolderArgumentType;
import net.minecraft.command.argument.ScoreboardCriterionArgumentType;
import net.minecraft.command.argument.ScoreboardObjectiveArgumentType;
import net.minecraft.command.argument.ScoreboardSlotArgumentType;
import net.minecraft.command.argument.TextArgumentType;
import net.minecraft.scoreboard.Scoreboard;
import net.minecraft.scoreboard.ScoreboardCriterion;
import net.minecraft.scoreboard.ScoreboardObjective;
import net.minecraft.scoreboard.ScoreboardPlayerScore;
import net.minecraft.scoreboard.ServerScoreboard;
import net.minecraft.server.command.CommandManager;
import net.minecraft.server.command.ServerCommandSource;
import net.minecraft.text.Text;
import net.minecraft.text.Texts;

public class ScoreboardCommand {
    private static final SimpleCommandExceptionType OBJECTIVES_ADD_DUPLICATE_EXCEPTION = new SimpleCommandExceptionType(Text.translatable("commands.scoreboard.objectives.add.duplicate"));
    private static final SimpleCommandExceptionType OBJECTIVES_DISPLAY_ALREADY_EMPTY_EXCEPTION = new SimpleCommandExceptionType(Text.translatable("commands.scoreboard.objectives.display.alreadyEmpty"));
    private static final SimpleCommandExceptionType OBJECTIVES_DISPLAY_ALREADY_SET_EXCEPTION = new SimpleCommandExceptionType(Text.translatable("commands.scoreboard.objectives.display.alreadySet"));
    private static final SimpleCommandExceptionType PLAYERS_ENABLE_FAILED_EXCEPTION = new SimpleCommandExceptionType(Text.translatable("commands.scoreboard.players.enable.failed"));
    private static final SimpleCommandExceptionType PLAYERS_ENABLE_INVALID_EXCEPTION = new SimpleCommandExceptionType(Text.translatable("commands.scoreboard.players.enable.invalid"));
    private static final Dynamic2CommandExceptionType PLAYERS_GET_NULL_EXCEPTION = new Dynamic2CommandExceptionType((objective, target) -> Text.translatable("commands.scoreboard.players.get.null", objective, target));

    public static void register(CommandDispatcher<ServerCommandSource> dispatcher) {
        dispatcher.register((LiteralArgumentBuilder)((LiteralArgumentBuilder)((LiteralArgumentBuilder)CommandManager.literal("scoreboard").requires(source -> source.hasPermissionLevel(2))).then(((LiteralArgumentBuilder)((LiteralArgumentBuilder)((LiteralArgumentBuilder)((LiteralArgumentBuilder)CommandManager.literal("objectives").then((ArgumentBuilder<ServerCommandSource, ?>)CommandManager.literal("list").executes(context -> ScoreboardCommand.executeListObjectives((ServerCommandSource)context.getSource())))).then(CommandManager.literal("add").then((ArgumentBuilder<ServerCommandSource, ?>)CommandManager.argument("objective", StringArgumentType.word()).then((ArgumentBuilder<ServerCommandSource, ?>)((RequiredArgumentBuilder)CommandManager.argument("criteria", ScoreboardCriterionArgumentType.scoreboardCriterion()).executes(context -> ScoreboardCommand.executeAddObjective((ServerCommandSource)context.getSource(), StringArgumentType.getString(context, "objective"), ScoreboardCriterionArgumentType.getCriterion(context, "criteria"), Text.literal(StringArgumentType.getString(context, "objective"))))).then(CommandManager.argument("displayName", TextArgumentType.text()).executes(context -> ScoreboardCommand.executeAddObjective((ServerCommandSource)context.getSource(), StringArgumentType.getString(context, "objective"), ScoreboardCriterionArgumentType.getCriterion(context, "criteria"), TextArgumentType.getTextArgument(context, "displayName")))))))).then(CommandManager.literal("modify").then((ArgumentBuilder<ServerCommandSource, ?>)((RequiredArgumentBuilder)CommandManager.argument("objective", ScoreboardObjectiveArgumentType.scoreboardObjective()).then((ArgumentBuilder<ServerCommandSource, ?>)CommandManager.literal("displayname").then((ArgumentBuilder<ServerCommandSource, ?>)CommandManager.argument("displayName", TextArgumentType.text()).executes(context -> ScoreboardCommand.executeModifyObjective((ServerCommandSource)context.getSource(), ScoreboardObjectiveArgumentType.getObjective(context, "objective"), TextArgumentType.getTextArgument(context, "displayName")))))).then(ScoreboardCommand.makeRenderTypeArguments())))).then(CommandManager.literal("remove").then((ArgumentBuilder<ServerCommandSource, ?>)CommandManager.argument("objective", ScoreboardObjectiveArgumentType.scoreboardObjective()).executes(context -> ScoreboardCommand.executeRemoveObjective((ServerCommandSource)context.getSource(), ScoreboardObjectiveArgumentType.getObjective(context, "objective")))))).then(CommandManager.literal("setdisplay").then((ArgumentBuilder<ServerCommandSource, ?>)((RequiredArgumentBuilder)CommandManager.argument("slot", ScoreboardSlotArgumentType.scoreboardSlot()).executes(context -> ScoreboardCommand.executeClearDisplay((ServerCommandSource)context.getSource(), ScoreboardSlotArgumentType.getScoreboardSlot(context, "slot")))).then(CommandManager.argument("objective", ScoreboardObjectiveArgumentType.scoreboardObjective()).executes(context -> ScoreboardCommand.executeSetDisplay((ServerCommandSource)context.getSource(), ScoreboardSlotArgumentType.getScoreboardSlot(context, "slot"), ScoreboardObjectiveArgumentType.getObjective(context, "objective")))))))).then(((LiteralArgumentBuilder)((LiteralArgumentBuilder)((LiteralArgumentBuilder)((LiteralArgumentBuilder)((LiteralArgumentBuilder)((LiteralArgumentBuilder)((LiteralArgumentBuilder)CommandManager.literal("players").then((ArgumentBuilder<ServerCommandSource, ?>)((LiteralArgumentBuilder)CommandManager.literal("list").executes(context -> ScoreboardCommand.executeListPlayers((ServerCommandSource)context.getSource()))).then(CommandManager.argument("target", ScoreHolderArgumentType.scoreHolder()).suggests(ScoreHolderArgumentType.SUGGESTION_PROVIDER).executes(context -> ScoreboardCommand.executeListScores((ServerCommandSource)context.getSource(), ScoreHolderArgumentType.getScoreHolder(context, "target")))))).then(CommandManager.literal("set").then((ArgumentBuilder<ServerCommandSource, ?>)CommandManager.argument("targets", ScoreHolderArgumentType.scoreHolders()).suggests(ScoreHolderArgumentType.SUGGESTION_PROVIDER).then((ArgumentBuilder<ServerCommandSource, ?>)CommandManager.argument("objective", ScoreboardObjectiveArgumentType.scoreboardObjective()).then((ArgumentBuilder<ServerCommandSource, ?>)CommandManager.argument("score", IntegerArgumentType.integer()).executes(context -> ScoreboardCommand.executeSet((ServerCommandSource)context.getSource(), ScoreHolderArgumentType.getScoreboardScoreHolders(context, "targets"), ScoreboardObjectiveArgumentType.getWritableObjective(context, "objective"), IntegerArgumentType.getInteger(context, "score")))))))).then(CommandManager.literal("get").then((ArgumentBuilder<ServerCommandSource, ?>)CommandManager.argument("target", ScoreHolderArgumentType.scoreHolder()).suggests(ScoreHolderArgumentType.SUGGESTION_PROVIDER).then((ArgumentBuilder<ServerCommandSource, ?>)CommandManager.argument("objective", ScoreboardObjectiveArgumentType.scoreboardObjective()).executes(context -> ScoreboardCommand.executeGet((ServerCommandSource)context.getSource(), ScoreHolderArgumentType.getScoreHolder(context, "target"), ScoreboardObjectiveArgumentType.getObjective(context, "objective"))))))).then(CommandManager.literal("add").then((ArgumentBuilder<ServerCommandSource, ?>)CommandManager.argument("targets", ScoreHolderArgumentType.scoreHolders()).suggests(ScoreHolderArgumentType.SUGGESTION_PROVIDER).then((ArgumentBuilder<ServerCommandSource, ?>)CommandManager.argument("objective", ScoreboardObjectiveArgumentType.scoreboardObjective()).then((ArgumentBuilder<ServerCommandSource, ?>)CommandManager.argument("score", IntegerArgumentType.integer(0)).executes(context -> ScoreboardCommand.executeAdd((ServerCommandSource)context.getSource(), ScoreHolderArgumentType.getScoreboardScoreHolders(context, "targets"), ScoreboardObjectiveArgumentType.getWritableObjective(context, "objective"), IntegerArgumentType.getInteger(context, "score")))))))).then(CommandManager.literal("remove").then((ArgumentBuilder<ServerCommandSource, ?>)CommandManager.argument("targets", ScoreHolderArgumentType.scoreHolders()).suggests(ScoreHolderArgumentType.SUGGESTION_PROVIDER).then((ArgumentBuilder<ServerCommandSource, ?>)CommandManager.argument("objective", ScoreboardObjectiveArgumentType.scoreboardObjective()).then((ArgumentBuilder<ServerCommandSource, ?>)CommandManager.argument("score", IntegerArgumentType.integer(0)).executes(context -> ScoreboardCommand.executeRemove((ServerCommandSource)context.getSource(), ScoreHolderArgumentType.getScoreboardScoreHolders(context, "targets"), ScoreboardObjectiveArgumentType.getWritableObjective(context, "objective"), IntegerArgumentType.getInteger(context, "score")))))))).then(CommandManager.literal("reset").then((ArgumentBuilder<ServerCommandSource, ?>)((RequiredArgumentBuilder)CommandManager.argument("targets", ScoreHolderArgumentType.scoreHolders()).suggests(ScoreHolderArgumentType.SUGGESTION_PROVIDER).executes(context -> ScoreboardCommand.executeReset((ServerCommandSource)context.getSource(), ScoreHolderArgumentType.getScoreboardScoreHolders(context, "targets")))).then(CommandManager.argument("objective", ScoreboardObjectiveArgumentType.scoreboardObjective()).executes(context -> ScoreboardCommand.executeReset((ServerCommandSource)context.getSource(), ScoreHolderArgumentType.getScoreboardScoreHolders(context, "targets"), ScoreboardObjectiveArgumentType.getObjective(context, "objective"))))))).then(CommandManager.literal("enable").then((ArgumentBuilder<ServerCommandSource, ?>)CommandManager.argument("targets", ScoreHolderArgumentType.scoreHolders()).suggests(ScoreHolderArgumentType.SUGGESTION_PROVIDER).then((ArgumentBuilder<ServerCommandSource, ?>)CommandManager.argument("objective", ScoreboardObjectiveArgumentType.scoreboardObjective()).suggests((context, builder) -> ScoreboardCommand.suggestDisabled((ServerCommandSource)context.getSource(), ScoreHolderArgumentType.getScoreboardScoreHolders(context, "targets"), builder)).executes(context -> ScoreboardCommand.executeEnable((ServerCommandSource)context.getSource(), ScoreHolderArgumentType.getScoreboardScoreHolders(context, "targets"), ScoreboardObjectiveArgumentType.getObjective(context, "objective"))))))).then(CommandManager.literal("operation").then((ArgumentBuilder<ServerCommandSource, ?>)CommandManager.argument("targets", ScoreHolderArgumentType.scoreHolders()).suggests(ScoreHolderArgumentType.SUGGESTION_PROVIDER).then((ArgumentBuilder<ServerCommandSource, ?>)CommandManager.argument("targetObjective", ScoreboardObjectiveArgumentType.scoreboardObjective()).then((ArgumentBuilder<ServerCommandSource, ?>)CommandManager.argument("operation", OperationArgumentType.operation()).then((ArgumentBuilder<ServerCommandSource, ?>)CommandManager.argument("source", ScoreHolderArgumentType.scoreHolders()).suggests(ScoreHolderArgumentType.SUGGESTION_PROVIDER).then((ArgumentBuilder<ServerCommandSource, ?>)CommandManager.argument("sourceObjective", ScoreboardObjectiveArgumentType.scoreboardObjective()).executes(context -> ScoreboardCommand.executeOperation((ServerCommandSource)context.getSource(), ScoreHolderArgumentType.getScoreboardScoreHolders(context, "targets"), ScoreboardObjectiveArgumentType.getWritableObjective(context, "targetObjective"), OperationArgumentType.getOperation(context, "operation"), ScoreHolderArgumentType.getScoreboardScoreHolders(context, "source"), ScoreboardObjectiveArgumentType.getObjective(context, "sourceObjective")))))))))));
    }

    private static LiteralArgumentBuilder<ServerCommandSource> makeRenderTypeArguments() {
        LiteralArgumentBuilder<ServerCommandSource> literalArgumentBuilder = CommandManager.literal("rendertype");
        for (ScoreboardCriterion.RenderType renderType : ScoreboardCriterion.RenderType.values()) {
            literalArgumentBuilder.then((ArgumentBuilder<ServerCommandSource, ?>)CommandManager.literal(renderType.getName()).executes(context -> ScoreboardCommand.executeModifyRenderType((ServerCommandSource)context.getSource(), ScoreboardObjectiveArgumentType.getObjective(context, "objective"), renderType)));
        }
        return literalArgumentBuilder;
    }

    private static CompletableFuture<Suggestions> suggestDisabled(ServerCommandSource source, Collection<String> targets, SuggestionsBuilder builder) {
        ArrayList<String> list = Lists.newArrayList();
        ServerScoreboard scoreboard = source.getServer().getScoreboard();
        for (ScoreboardObjective scoreboardObjective : scoreboard.getObjectives()) {
            if (scoreboardObjective.getCriterion() != ScoreboardCriterion.TRIGGER) continue;
            boolean bl = false;
            for (String string : targets) {
                if (scoreboard.playerHasObjective(string, scoreboardObjective) && !scoreboard.getPlayerScore(string, scoreboardObjective).isLocked()) continue;
                bl = true;
                break;
            }
            if (!bl) continue;
            list.add(scoreboardObjective.getName());
        }
        return CommandSource.suggestMatching(list, builder);
    }

    private static int executeGet(ServerCommandSource source, String target, ScoreboardObjective objective) throws CommandSyntaxException {
        ServerScoreboard scoreboard = source.getServer().getScoreboard();
        if (!scoreboard.playerHasObjective(target, objective)) {
            throw PLAYERS_GET_NULL_EXCEPTION.create(objective.getName(), target);
        }
        ScoreboardPlayerScore scoreboardPlayerScore = scoreboard.getPlayerScore(target, objective);
        source.sendFeedback(() -> Text.translatable("commands.scoreboard.players.get.success", target, scoreboardPlayerScore.getScore(), objective.toHoverableText()), false);
        return scoreboardPlayerScore.getScore();
    }

    private static int executeOperation(ServerCommandSource source, Collection<String> targets, ScoreboardObjective targetObjective, OperationArgumentType.Operation operation, Collection<String> sources, ScoreboardObjective sourceObjectives) throws CommandSyntaxException {
        ServerScoreboard scoreboard = source.getServer().getScoreboard();
        int i = 0;
        for (String string : targets) {
            ScoreboardPlayerScore scoreboardPlayerScore = scoreboard.getPlayerScore(string, targetObjective);
            for (String string2 : sources) {
                ScoreboardPlayerScore scoreboardPlayerScore2 = scoreboard.getPlayerScore(string2, sourceObjectives);
                operation.apply(scoreboardPlayerScore, scoreboardPlayerScore2);
            }
            i += scoreboardPlayerScore.getScore();
        }
        if (targets.size() == 1) {
            int j = i;
            source.sendFeedback(() -> Text.translatable("commands.scoreboard.players.operation.success.single", targetObjective.toHoverableText(), targets.iterator().next(), j), true);
        } else {
            source.sendFeedback(() -> Text.translatable("commands.scoreboard.players.operation.success.multiple", targetObjective.toHoverableText(), targets.size()), true);
        }
        return i;
    }

    private static int executeEnable(ServerCommandSource source, Collection<String> targets, ScoreboardObjective objective) throws CommandSyntaxException {
        if (objective.getCriterion() != ScoreboardCriterion.TRIGGER) {
            throw PLAYERS_ENABLE_INVALID_EXCEPTION.create();
        }
        ServerScoreboard scoreboard = source.getServer().getScoreboard();
        int i = 0;
        for (String string : targets) {
            ScoreboardPlayerScore scoreboardPlayerScore = scoreboard.getPlayerScore(string, objective);
            if (!scoreboardPlayerScore.isLocked()) continue;
            scoreboardPlayerScore.setLocked(false);
            ++i;
        }
        if (i == 0) {
            throw PLAYERS_ENABLE_FAILED_EXCEPTION.create();
        }
        if (targets.size() == 1) {
            source.sendFeedback(() -> Text.translatable("commands.scoreboard.players.enable.success.single", objective.toHoverableText(), targets.iterator().next()), true);
        } else {
            source.sendFeedback(() -> Text.translatable("commands.scoreboard.players.enable.success.multiple", objective.toHoverableText(), targets.size()), true);
        }
        return i;
    }

    private static int executeReset(ServerCommandSource source, Collection<String> targets) {
        ServerScoreboard scoreboard = source.getServer().getScoreboard();
        for (String string : targets) {
            scoreboard.resetPlayerScore(string, null);
        }
        if (targets.size() == 1) {
            source.sendFeedback(() -> Text.translatable("commands.scoreboard.players.reset.all.single", targets.iterator().next()), true);
        } else {
            source.sendFeedback(() -> Text.translatable("commands.scoreboard.players.reset.all.multiple", targets.size()), true);
        }
        return targets.size();
    }

    private static int executeReset(ServerCommandSource source, Collection<String> targets, ScoreboardObjective objective) {
        ServerScoreboard scoreboard = source.getServer().getScoreboard();
        for (String string : targets) {
            scoreboard.resetPlayerScore(string, objective);
        }
        if (targets.size() == 1) {
            source.sendFeedback(() -> Text.translatable("commands.scoreboard.players.reset.specific.single", objective.toHoverableText(), targets.iterator().next()), true);
        } else {
            source.sendFeedback(() -> Text.translatable("commands.scoreboard.players.reset.specific.multiple", objective.toHoverableText(), targets.size()), true);
        }
        return targets.size();
    }

    private static int executeSet(ServerCommandSource source, Collection<String> targets, ScoreboardObjective objective, int score) {
        ServerScoreboard scoreboard = source.getServer().getScoreboard();
        for (String string : targets) {
            ScoreboardPlayerScore scoreboardPlayerScore = scoreboard.getPlayerScore(string, objective);
            scoreboardPlayerScore.setScore(score);
        }
        if (targets.size() == 1) {
            source.sendFeedback(() -> Text.translatable("commands.scoreboard.players.set.success.single", objective.toHoverableText(), targets.iterator().next(), score), true);
        } else {
            source.sendFeedback(() -> Text.translatable("commands.scoreboard.players.set.success.multiple", objective.toHoverableText(), targets.size(), score), true);
        }
        return score * targets.size();
    }

    private static int executeAdd(ServerCommandSource source, Collection<String> targets, ScoreboardObjective objective, int score) {
        ServerScoreboard scoreboard = source.getServer().getScoreboard();
        int i = 0;
        for (String string : targets) {
            ScoreboardPlayerScore scoreboardPlayerScore = scoreboard.getPlayerScore(string, objective);
            scoreboardPlayerScore.setScore(scoreboardPlayerScore.getScore() + score);
            i += scoreboardPlayerScore.getScore();
        }
        if (targets.size() == 1) {
            int j = i;
            source.sendFeedback(() -> Text.translatable("commands.scoreboard.players.add.success.single", score, objective.toHoverableText(), targets.iterator().next(), j), true);
        } else {
            source.sendFeedback(() -> Text.translatable("commands.scoreboard.players.add.success.multiple", score, objective.toHoverableText(), targets.size()), true);
        }
        return i;
    }

    private static int executeRemove(ServerCommandSource source, Collection<String> targets, ScoreboardObjective objective, int score) {
        ServerScoreboard scoreboard = source.getServer().getScoreboard();
        int i = 0;
        for (String string : targets) {
            ScoreboardPlayerScore scoreboardPlayerScore = scoreboard.getPlayerScore(string, objective);
            scoreboardPlayerScore.setScore(scoreboardPlayerScore.getScore() - score);
            i += scoreboardPlayerScore.getScore();
        }
        if (targets.size() == 1) {
            int j = i;
            source.sendFeedback(() -> Text.translatable("commands.scoreboard.players.remove.success.single", score, objective.toHoverableText(), targets.iterator().next(), j), true);
        } else {
            source.sendFeedback(() -> Text.translatable("commands.scoreboard.players.remove.success.multiple", score, objective.toHoverableText(), targets.size()), true);
        }
        return i;
    }

    private static int executeListPlayers(ServerCommandSource source) {
        Collection<String> collection = source.getServer().getScoreboard().getKnownPlayers();
        if (collection.isEmpty()) {
            source.sendFeedback(() -> Text.translatable("commands.scoreboard.players.list.empty"), false);
        } else {
            source.sendFeedback(() -> Text.translatable("commands.scoreboard.players.list.success", collection.size(), Texts.joinOrdered(collection)), false);
        }
        return collection.size();
    }

    private static int executeListScores(ServerCommandSource source, String target) {
        Map<ScoreboardObjective, ScoreboardPlayerScore> map = source.getServer().getScoreboard().getPlayerObjectives(target);
        if (map.isEmpty()) {
            source.sendFeedback(() -> Text.translatable("commands.scoreboard.players.list.entity.empty", target), false);
        } else {
            source.sendFeedback(() -> Text.translatable("commands.scoreboard.players.list.entity.success", target, map.size()), false);
            for (Map.Entry<ScoreboardObjective, ScoreboardPlayerScore> entry : map.entrySet()) {
                source.sendFeedback(() -> Text.translatable("commands.scoreboard.players.list.entity.entry", ((ScoreboardObjective)entry.getKey()).toHoverableText(), ((ScoreboardPlayerScore)entry.getValue()).getScore()), false);
            }
        }
        return map.size();
    }

    private static int executeClearDisplay(ServerCommandSource source, int slot) throws CommandSyntaxException {
        ServerScoreboard scoreboard = source.getServer().getScoreboard();
        if (scoreboard.getObjectiveForSlot(slot) == null) {
            throw OBJECTIVES_DISPLAY_ALREADY_EMPTY_EXCEPTION.create();
        }
        ((Scoreboard)scoreboard).setObjectiveSlot(slot, null);
        source.sendFeedback(() -> Text.translatable("commands.scoreboard.objectives.display.cleared", Scoreboard.getDisplaySlotNames()[slot]), true);
        return 0;
    }

    private static int executeSetDisplay(ServerCommandSource source, int slot, ScoreboardObjective objective) throws CommandSyntaxException {
        ServerScoreboard scoreboard = source.getServer().getScoreboard();
        if (scoreboard.getObjectiveForSlot(slot) == objective) {
            throw OBJECTIVES_DISPLAY_ALREADY_SET_EXCEPTION.create();
        }
        ((Scoreboard)scoreboard).setObjectiveSlot(slot, objective);
        source.sendFeedback(() -> Text.translatable("commands.scoreboard.objectives.display.set", Scoreboard.getDisplaySlotNames()[slot], objective.getDisplayName()), true);
        return 0;
    }

    private static int executeModifyObjective(ServerCommandSource source, ScoreboardObjective objective, Text displayName) {
        if (!objective.getDisplayName().equals(displayName)) {
            objective.setDisplayName(displayName);
            source.sendFeedback(() -> Text.translatable("commands.scoreboard.objectives.modify.displayname", objective.getName(), objective.toHoverableText()), true);
        }
        return 0;
    }

    private static int executeModifyRenderType(ServerCommandSource source, ScoreboardObjective objective, ScoreboardCriterion.RenderType type) {
        if (objective.getRenderType() != type) {
            objective.setRenderType(type);
            source.sendFeedback(() -> Text.translatable("commands.scoreboard.objectives.modify.rendertype", objective.toHoverableText()), true);
        }
        return 0;
    }

    private static int executeRemoveObjective(ServerCommandSource source, ScoreboardObjective objective) {
        ServerScoreboard scoreboard = source.getServer().getScoreboard();
        scoreboard.removeObjective(objective);
        source.sendFeedback(() -> Text.translatable("commands.scoreboard.objectives.remove.success", objective.toHoverableText()), true);
        return scoreboard.getObjectives().size();
    }

    private static int executeAddObjective(ServerCommandSource source, String objective, ScoreboardCriterion criteria, Text displayName) throws CommandSyntaxException {
        ServerScoreboard scoreboard = source.getServer().getScoreboard();
        if (scoreboard.getNullableObjective(objective) != null) {
            throw OBJECTIVES_ADD_DUPLICATE_EXCEPTION.create();
        }
        scoreboard.addObjective(objective, criteria, displayName, criteria.getDefaultRenderType());
        ScoreboardObjective scoreboardObjective = scoreboard.getNullableObjective(objective);
        source.sendFeedback(() -> Text.translatable("commands.scoreboard.objectives.add.success", scoreboardObjective.toHoverableText()), true);
        return scoreboard.getObjectives().size();
    }

    private static int executeListObjectives(ServerCommandSource source) {
        Collection<ScoreboardObjective> collection = source.getServer().getScoreboard().getObjectives();
        if (collection.isEmpty()) {
            source.sendFeedback(() -> Text.translatable("commands.scoreboard.objectives.list.empty"), false);
        } else {
            source.sendFeedback(() -> Text.translatable("commands.scoreboard.objectives.list.success", collection.size(), Texts.join(collection, ScoreboardObjective::toHoverableText)), false);
        }
        return collection.size();
    }
}

