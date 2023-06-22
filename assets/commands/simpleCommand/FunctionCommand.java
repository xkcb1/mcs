/*
 * Decompiled with CFR 0.2.0 (FabricMC d28b102d).
 */
package net.minecraft.server.command;

import com.mojang.brigadier.CommandDispatcher;
import com.mojang.brigadier.builder.LiteralArgumentBuilder;
import com.mojang.brigadier.suggestion.SuggestionProvider;
import java.util.Collection;
import java.util.OptionalInt;
import net.minecraft.command.CommandSource;
import net.minecraft.command.argument.CommandFunctionArgumentType;
import net.minecraft.server.command.CommandManager;
import net.minecraft.server.command.ServerCommandSource;
import net.minecraft.server.function.CommandFunction;
import net.minecraft.server.function.CommandFunctionManager;
import net.minecraft.text.Text;
import org.apache.commons.lang3.mutable.MutableObject;

public class FunctionCommand {
    public static final SuggestionProvider<ServerCommandSource> SUGGESTION_PROVIDER = (context, builder) -> {
        CommandFunctionManager commandFunctionManager = ((ServerCommandSource)context.getSource()).getServer().getCommandFunctionManager();
        CommandSource.suggestIdentifiers(commandFunctionManager.getFunctionTags(), builder, "#");
        return CommandSource.suggestIdentifiers(commandFunctionManager.getAllFunctions(), builder);
    };

    public static void register(CommandDispatcher<ServerCommandSource> dispatcher) {
        dispatcher.register((LiteralArgumentBuilder)((LiteralArgumentBuilder)CommandManager.literal("function").requires(source -> source.hasPermissionLevel(2))).then(CommandManager.argument("name", CommandFunctionArgumentType.commandFunction()).suggests(SUGGESTION_PROVIDER).executes(context -> FunctionCommand.execute((ServerCommandSource)context.getSource(), CommandFunctionArgumentType.getFunctions(context, "name")))));
    }

    private static int execute(ServerCommandSource source, Collection<CommandFunction> functions) {
        int i = 0;
        boolean bl = false;
        for (CommandFunction commandFunction : functions) {
            MutableObject<OptionalInt> mutableObject = new MutableObject<OptionalInt>(OptionalInt.empty());
            int j = source.getServer().getCommandFunctionManager().execute(commandFunction, source.withSilent().withMaxLevel(2).withReturnValueConsumer(value -> mutableObject.setValue(OptionalInt.of(value))));
            OptionalInt optionalInt = mutableObject.getValue();
            i += optionalInt.orElse(j);
            bl |= optionalInt.isPresent();
        }
        int k = i;
        if (functions.size() == 1) {
            if (bl) {
                source.sendFeedback(() -> Text.translatable("commands.function.success.single.result", k, ((CommandFunction)functions.iterator().next()).getId()), true);
            } else {
                source.sendFeedback(() -> Text.translatable("commands.function.success.single", k, ((CommandFunction)functions.iterator().next()).getId()), true);
            }
        } else if (bl) {
            source.sendFeedback(() -> Text.translatable("commands.function.success.multiple.result", functions.size()), true);
        } else {
            source.sendFeedback(() -> Text.translatable("commands.function.success.multiple", k, functions.size()), true);
        }
        return i;
    }
}

