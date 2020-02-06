import sublime
import sublime_plugin

import re

from dobby.emojis import EMOJIS

class DobbyCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # self.view.insert(edit, 0, "Hello, World!")
        contents = self.view.substr(sublime.Region(0, self.view.size()))
        region = sublime.Region(0, self.view.size())
        self.view.replace(edit, region, self.emojify(contents))

    def emojify(self, contents):
        return self.emoji_replace(EMOJIS, contents)

    def emoji_replace(self, edict, text):
        # create a regular expression from all of the dictionary keys
        regex = re.compile("|".join(map(re.escape, edict.keys(  ))))
        # for each match, look up the corresponding value in the dictionary
        return regex.sub(lambda match: edict[match.group(0)], text)



class DobbyCompletionsListener(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        source = EMOJIS.keys()
        completions = [[key + " " + EMOJIS[key] , EMOJIS[key]] for key in source if prefix in key]
        if not completions:
            return None
        return completions