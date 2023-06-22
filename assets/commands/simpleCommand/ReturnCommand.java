/*
 * Decompiled with CFR 0.2.0 (FabricMC d28b102d).
 */
package net.minecraft.server.command;

import com.mojang.brigadier.CommandDispatcher;
import com.mojang.brigadier.arguments.IntegerArgumentType;
import com.mojang.brigadier.builder.LiteralArgumentBuilder;
import net.minecraft.server.command.CommandManager;
import net.minecraft.server.command.ServerCommandSource;

public class ReturnCommand {
    public static void register(CommandDispatcher<ServerCommandSource> dispatcher) {
        dispatcher.register((LiteralArgumentBuilder)((LiteralArgumentBuilder)CommandManager.literal("return").requires(source -> source.hasPermissionLevel(2))).then(CommandManager.argument("value", IntegerArgumentType.integer()).executes(context -> ReturnCommand.execute((ServerCommandSource)context.getSource(), IntegerArgumentType.getInteger(context, "value")))));
    }

    private static int execute(ServerCommandSource source, int value) {
        source.getReturnValueConsumer().accept(value);
        return value;
    }
}

