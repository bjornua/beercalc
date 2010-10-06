#ifndef _BEERCALC_MAINWINDOW
#define BEERCALC_MAINWINDOW
#include "wx/wx.h"

enum {
    ID_Quit = 1,
    ID_About = 2,
};

class MainApp: public wxApp {
    virtual bool OnInit();
};

class MyFrame: public wxFrame {
public:
    MyFrame(const wxString& title, const wxPoint& pos, const wxSize& size);

    void OnQuit(wxCommandEvent& event);
    void OnAbout(wxCommandEvent& event);

    DECLARE_EVENT_TABLE()
};

BEGIN_EVENT_TABLE(MyFrame, wxFrame)
EVT_MENU(ID_Quit, MyFrame::OnQuit)
EVT_MENU(ID_About, MyFrame::OnAbout)
END_EVENT_TABLE()


#endif
