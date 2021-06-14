# GUI-with-TKINTER
Why GUI? When we develop an Machine Learning MODEL to show someone, then it is most feasible to show them by GUI interface. As it is convince for everyone to use it.

Python provides various options for developing graphical user interfaces (GUIs). Most important are listed below.
Tkinter − Tkinter is the Python interface to the Tk GUI toolkit shipped with Python. We would look this option in this chapter.
wxPython − This is an open-source Python interface for wxWindows http://wxpython.org.
JPython − JPython is a Python port for Java which gives Python scripts seamless access to Java class libraries on the local machine http://www.jython.org.

Tkinter is the standard GUI library for Python. Python when combined with Tkinter provides a fast and easy way to create GUI applications. Tkinter provides a powerful object-oriented interface to the Tk GUI toolkit.
Creating a GUI application using Tkinter is an easy task. All you need to do is perform the following steps −
Import the Tkinter module.
Create the GUI application main window.
Add one or more of the above-mentioned widgets to the GUI application.
Enter the main event loop to take action against each event triggered by the user.


import Tkinter 
top = Tkinter.Tk()

top.mainloop()

mainloop() is used when your application is ready to run.
mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event as long as the window is not closed.

