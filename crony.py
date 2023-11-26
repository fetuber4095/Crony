#!/opentty.py rundll
# -*- coding: utf-8 -*-
#
#  Copyright (C) 2023 "Mr. Lima" [crony.py]
#
#  This code is part of OpenTTY Package Repository - Crony Project
#  
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#  
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#  
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

from opentty import *



class Crony(OpenTTY):
	def __init__(self, lang="pt"):
		self.lang = lang

		self.filter = json.load(open(f"filter-{self.lang}.json", "r"))



	def client(self):
		while True:
			try: 
				app.clear()

				quest = input("\n| Quest: ").strip()


				sel = self.run_filter(quest)
				input(sel)

			except (KeyboardInterrupt, EOFError): return



	def run_filter(self, quest):
		for method in self.filter:
			for keyword in method:
				if quest.split()[0] == keyword:

					return method

		return 


crony = Crony()
crony.client()