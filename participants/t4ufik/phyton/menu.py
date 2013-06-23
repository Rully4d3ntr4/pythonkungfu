#!/usr/bin/env 

import wx

class bucky(wx.frame):

	def __init__(self,parent,id):
		wx.frame.__init__(self,parent,id,'Frame aka window', size=(300,200))
		panel=wx.Panel(self)


		status=self.CreateStatusBar()
		menubar=wx.MenuBar()
		first=wx.Menu()
		second=wx.Menu()
		first.Append(wx.NewId(),"New window","This is a new window")
		first.Append(wx.NewId(),"open...","this will open new window")
		menubar.Append(first,"File")
		menubar.Append(second,"edit")
		self.SetMenuBar(menubar)


if __name__ == '__main__':
	app=wx.PySimpleApp()
	frame=bucky(parent=None,id=-1)
	frame.Show()
	app.MainLoop()