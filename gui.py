#Boa:Frame:Frame1

import wx
import gui_background

gb = gui_background.FindPath()
gb.load()

def create(parent):
	return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1CLEAR_BUTTON, wxID_FRAME1DEBUG, 
 wxID_FRAME1DESTINATIONS, wxID_FRAME1DESTINATION_INPUT, wxID_FRAME1HISTORY, 
 wxID_FRAME1ORIGINS, wxID_FRAME1ORIGIN_INPUT, wxID_FRAME1PANEL1, 
 wxID_FRAME1RECENT_SEARCHES, wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, 
 wxID_FRAME1STATICTEXT3, wxID_FRAME1STATICTEXT4, wxID_FRAME1QUIT_BUTTON,
 wxID_FRAME1RAND1_BUTTON, wxID_FRAME1RAND2_BUTTON,
] = [wx.NewId() for _init_ctrls in range(18)]

class Frame1(wx.Frame):
	def _init_ctrls(self, prnt):
		# generated method, don't edit
		wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
			  pos=wx.Point(576, 235), size=wx.Size(1936, 1176),
			  style=wx.DEFAULT_FRAME_STYLE, title='Frame1')
		self.SetClientSize(wx.Size(1920, 1138))
		self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
			  pos=wx.Point(0, 0), size=wx.Size(1920, 1138),
			  style=wx.TAB_TRAVERSAL)
		self.panel1.SetBackgroundColour('#5CADFF')
		self.Maximize()
		self.Origin_input = wx.TextCtrl(id=wxID_FRAME1ORIGIN_INPUT,
			  name=u'Origin_input', parent=self.panel1, pos=wx.Point(656, 24),
			  size=wx.Size(144, 32), style=0, value=u'')
		self.Origin_input.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
			  False, u'Tahoma'))

		self.Destination_input = wx.TextCtrl(id=wxID_FRAME1DESTINATION_INPUT,
			  name=u'Destination_input', parent=self.panel1, pos=wx.Point(1248,
			  24), size=wx.Size(136, 32), style=0, value=u'')
		self.Destination_input.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL,
			  wx.NORMAL, False, u'Tahoma'))

		self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
			  label=u'Start User:', name='staticText1', parent=self.panel1,
			  pos=wx.Point(552, 24), size=wx.Size(90, 23), style=0)
		self.staticText1.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
			  False, u'Tahoma'))
		self.staticText1.SetForegroundColour(wx.Colour(255, 255, 255))

		self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
			  label=u'End User:', name='staticText2', parent=self.panel1,
			  pos=wx.Point(1152, 24), size=wx.Size(83, 23), style=0)
		self.staticText2.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
			  False, u'Tahoma'))
		self.staticText2.SetForegroundColour(wx.Colour(255, 255, 255))
		self.staticText2.Show(True)

		self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label=u'Go',
			  name='button1', parent=self.panel1, pos=wx.Point(905, 112),
			  size=wx.Size(110, 40), style=0)
		self.button1.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
			  u'Tahoma'))
		self.button1.Bind(wx.EVT_BUTTON, self.OnGo, id=wxID_FRAME1BUTTON1)

		self.History = wx.Panel(id=wxID_FRAME1HISTORY, name=u'History',
			  parent=self.panel1, pos=wx.Point(64, 792), size=wx.Size(416, 280),
			  style=wx.TAB_TRAVERSAL)
		self.History.SetBackgroundColour('#5CADFF')
		self.History.SetForegroundColour('#FFFFFF')

		self.Origins = wx.ListBox(choices=[], id=wxID_FRAME1ORIGINS,
			  name=u'Origins', parent=self.History, pos=wx.Point(32, 64),
			  size=wx.Size(144, 200), style=0)
		self.Origins.SetLabel(u'')
		self.Origins.SetHelpText(u'')
		self.Origins.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
			  u'Tahoma'))
		self.Origins.SetStringSelection(u'')
		self.Origins.SetToolTipString(u'Recently Used Origins')
		self.Origins.SetSelection(-1)
		self.Origins.Bind(wx.EVT_LISTBOX, self.OnOriginsListbox,
			  id=wxID_FRAME1ORIGINS)

		self.Destinations = wx.ListBox(choices=[], id=wxID_FRAME1DESTINATIONS,
			  name=u'Destinations', parent=self.History, pos=wx.Point(232, 64),
			  size=wx.Size(144, 200), style=0)
		self.Destinations.SetLabel(u'')
		self.Destinations.SetHelpText(u'')
		self.Destinations.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
			  False, u'Tahoma'))
		self.Destinations.SetToolTipString(u'Recently Used Destinations')
		self.Destinations.SetSelection(-1)
		self.Destinations.Show(True)
		self.Destinations.SetStringSelection(u'')
		self.Destinations.Bind(wx.EVT_LISTBOX, self.OnDestinationsListbox,
			  id=wxID_FRAME1DESTINATIONS)

		self.Clear_Button = wx.Button(id=wxID_FRAME1CLEAR_BUTTON,
			  label=u'Clear', name=u'Clear_Button', parent=self.panel1,
			  pos=wx.Point(912, 160), size=wx.Size(96, 32), style=0)
		self.Clear_Button.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
			  False, u'Tahoma'))
		self.Clear_Button.Bind(wx.EVT_BUTTON, self.OnClear_Button,
			  id=wxID_FRAME1CLEAR_BUTTON)

		self.Quit_Button = wx.Button(id=wxID_FRAME1QUIT_BUTTON,
			  label=u'Quit', name=u'Quit_Button', parent=self.panel1,
			  pos=wx.Point(912, 200), size=wx.Size(96, 32), style=0)
		self.Quit_Button.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
			  False, u'Tahoma'))
		self.Quit_Button.Bind(wx.EVT_BUTTON, self.OnQuit,
			  id=wxID_FRAME1QUIT_BUTTON)

		self.Rand1_Button = wx.Button(id=wxID_FRAME1RAND1_BUTTON,
			  label=u'Random', name=u'Rand1_Button', parent=self.panel1,
			  pos=wx.Point(680, 65), size=wx.Size(96, 32), style=0)
		self.Rand1_Button.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
			  False, u'Tahoma'))
		self.Rand1_Button.Bind(wx.EVT_BUTTON, self.OnRand1,
			  id=wxID_FRAME1RAND1_BUTTON)

		self.Rand2_Button = wx.Button(id=wxID_FRAME1RAND2_BUTTON,
			  label=u'Random', name=u'Rand2_Button', parent=self.panel1,
			  pos=wx.Point(1269, 65), size=wx.Size(96, 32), style=0)
		self.Rand2_Button.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
			  False, u'Tahoma'))
		self.Rand2_Button.Bind(wx.EVT_BUTTON, self.OnRand2,
			  id=wxID_FRAME1RAND2_BUTTON)

		self.Recent_Searches = wx.StaticText(id=wxID_FRAME1RECENT_SEARCHES,
			  label=u'Recent Seraches:', name=u'Recent_Searches',
			  parent=self.History, pos=wx.Point(136, 8), size=wx.Size(147, 23),
			  style=0)
		self.Recent_Searches.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
			  False, u'Tahoma'))

		self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
			  label=u'Destinations:', name='staticText3', parent=self.History,
			  pos=wx.Point(248, 40), size=wx.Size(108, 23), style=0)
		self.staticText3.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
			  False, u'Tahoma'))

		self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
			  label=u'Origins:', name='staticText4', parent=self.History,
			  pos=wx.Point(72, 40), size=wx.Size(65, 23), style=0)
		self.staticText4.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
			  False, u'Tahoma'))

	def __init__(self, parent):
		self._init_ctrls(parent)        



	def OnGo(self, event):
		if self.Origin_input.GetValue() != "" and self.Destination_input.GetValue() != "":
			start = self.Origin_input.GetValue()
			if start[0] != "@":
				start = "@" + start
			end = self.Destination_input.GetValue()
			if end[0] != "@":
				end = "@" + end
			self.OnClear_Button(0)
			if not gb.user_exists(start) and not gb.user_exists(end):
				DNE = wx.StaticText(label=" Users " + start[1:] + " and " + end[1:] + " do not exist.", parent=self.panel1, pos=(780, 500), size=wx.Size(350, 20))
				DNE.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Tahoma'))
				DNE.SetForegroundColour("white")
			elif not gb.user_exists(start):
				DNE = wx.StaticText(label=" User " + start[1:] + " does not exist.", parent=self.panel1, pos=(820, 500), size=wx.Size(350, 20))
				DNE.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Tahoma'))
				DNE.SetForegroundColour("white")
			elif not gb.user_exists(end):
				DNE = wx.StaticText(label=" User " + end[1:] + " does not exist.", parent=self.panel1, pos=(820, 500), size=wx.Size(350, 20))
				DNE.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Tahoma'))
				DNE.SetForegroundColour("white")
			else:
				o = [self.Origins.GetString(i) for i in range(self.Origins.GetCount())]
				d = [self.Destinations.GetString(i) for i in range(self.Destinations.GetCount())]
				if start[1:] not in o:
					o.append(start[1:])
				else:
					o.remove(start[1:])
					o.append(start[1:])
				if end[1:] not in d:
					d.append(end[1:])
				else:
					d.remove(end[1:])
					d.append(end[1:])
				self.Origins.Clear()
				self.Destinations.Clear()
				for item in o:
					self.Origins.Insert(item,0,None)
				for item in d:
					self.Destinations.Insert(item,0,None)
				self.Origin_input.Clear()
				self.Destination_input.Clear()
				self.Origins.DeselectAll()
				self.Destinations.DeselectAll()
				if not gb.path_exists(start, end):
					DNE = wx.StaticText(label="Sorry, there is no path between " + start[1:] + " and " + end[1:] + ".", parent=self.panel1, pos=(750, 500), size=wx.Size(350, 20))
					DNE.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Tahoma'))
					DNE.SetForegroundColour("white")
				else:
					DNE = wx.StaticText(label="Calculating path now. This will take a few minutes.", parent=self.panel1, pos=(740, 500), size=wx.Size(600, 30))
					DNE.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Tahoma'))
					DNE.SetForegroundColour("white")
					self.Update()
					path = gb.get_path(start, end)
					tweets = []
					for user in path:
						if user == path[len(path) - 1]:
							continue
						tweets.append(gb.get_tweet(user, path[path.index(user) + 1]))
					self.OnClear_Button(0)
					if len(path) > 1 and len(path) < 6:
						x_start = 300
						y_start = 300
						x_max = 1460
						y_max = 650
						x_interval = x_max-x_start
						y_interval = y_max-y_start
						x_incriment = x_interval/len(path)
						y_incriment = y_interval/len(path)
						count = 0
						for user in path:
							wx.StaticText(label=user, parent=self.panel1, pos=(x_start-125, y_start+20), size=wx.Size(125, 18)).SetBackgroundColour('white')
							wx.StaticText(label=tweets[count], parent=self.panel1, pos=(x_start+5, y_start+5), size=wx.Size(350, 50)).SetBackgroundColour('white')
							count += 1
							x_start +=x_incriment
							y_start += y_incriment
							
					if len(path) > 5 and len(path) < 11:
						x_start = 300
						y_start = 200
						x_max = 1460
						y_max = 850
						x_interval = x_max-x_start
						y_interval = y_max-y_start
						x_incriment = x_interval/len(path)
						y_incriment = y_interval/len(path)
						count = 0
						for user in path:
							wx.StaticText(label=user, parent=self.panel1, pos=(x_start-125, y_start+20), size=wx.Size(125, 18)).SetBackgroundColour('white')
							wx.StaticText(label=tweets[count], parent=self.panel1, pos=(x_start+5, y_start+5), size=wx.Size(350, 50)).SetBackgroundColour('white')
							count += 1
							x_start +=x_incriment
							y_start += y_incriment
							
					if len(path) > 10 and len(path) < 16:
						x_start = 150
						y_start = 200
						x_max = 1400
						y_max = 850
						x_interval = x_max-x_start
						y_interval = y_max-y_start
						x_incriment = x_interval/len(path)
						y_incriment = y_interval/len(path)
						count = 0
						for user in path:
							wx.StaticText(label=user, parent=self.panel1, pos=(x_start-95, y_start+8), size=wx.Size(95, 18)).SetBackgroundColour('white')
							wx.StaticText(label=tweets[count], parent=self.panel1, pos=(x_start+5, y_start+5), size=wx.Size(600, 25)).SetBackgroundColour('white')
							count += 1
							x_start +=x_incriment
							y_start += y_incriment
						
					if len(path) > 15 and len(path) < 21:
						x_start = 120
						y_start = 200
						x_max = 1400
						y_max = 850
						x_interval = x_max-x_start
						y_interval = y_max-y_start
						x_incriment = x_interval/len(path)
						y_incriment = y_interval/len(path)
						count = 0
						for user in path:
							wx.StaticText(label=user, parent=self.panel1, pos=(x_start-95, y_start+8), size=wx.Size(95, 18)).SetBackgroundColour('white')
							wx.StaticText(label=tweets[count], parent=self.panel1, pos=(x_start+5, y_start+5), size=wx.Size(600, 25)).SetBackgroundColour('white')
							count += 1
							x_start +=x_incriment
							y_start += y_incriment
								
					if len(path) > 20 and len(path) < 26:
						x_start = 100
						y_start = 200
						x_max = 1400
						y_max = 950
						x_interval = x_max-x_start
						y_interval = y_max-y_start
						x_incriment = x_interval/len(path)
						y_incriment = y_interval/len(path)
						count = 0
						for user in path:
							wx.StaticText(label=user, parent=self.panel1, pos=(x_start-90, y_start+8), size=wx.Size(90, 18)).SetBackgroundColour('white')
							wx.StaticText(label=tweets[count], parent=self.panel1, pos=(x_start+5, y_start+5), size=wx.Size(600, 25)).SetBackgroundColour('white')
							count += 1
							x_start +=x_incriment
							y_start += y_incriment

	def OnOriginsListbox(self, event):
		self.Origin_input.SetLabel(self.Origins.GetStringSelection())
		self.Update()

	def OnDestinationsListbox(self, event):
		self.Destination_input.SetLabel(self.Destinations.GetStringSelection())
		self.Update()
	def OnClear_Button(self, event):
		self.Origin_input.Clear()
		self.Destination_input.Clear()
		self.Update()
		dont_remove = [self.Origin_input, self.Destination_input, self.staticText1, self.staticText2,
					   self.button1, self.History, self.Origins, self.Destinations, self.Clear_Button,
					   self.Recent_Searches, self.staticText3, self.staticText4, self.Quit_Button,
					   self.Rand1_Button, self.Rand2_Button,
					  ]
		for child in self.panel1.GetChildren():
			if child not in dont_remove:
				child.Destroy()
	
	def OnRand1(self, event):
		self.Origin_input.Clear()
		self.Origin_input.WriteText(gb.get_random_user()[1:])
		self.Update()
		
	def OnRand2(self, event):
		self.Destination_input.Clear()
		self.Destination_input.WriteText(gb.get_random_user()[1:])
		self.Update()
		
	def OnQuit(self, event):
		self.Destroy()
		self.Update()
					
			#draw a blue line (thickness = 4)


if __name__ == '__main__':
	app = wx.PySimpleApp()
	frame = create(None)
	frame.Show()

	app.MainLoop()
	