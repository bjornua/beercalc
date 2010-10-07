#include "mainwindow.h"


IMPLEMENT_APP(MainApp)

bool MainApp::OnInit()
{
    MainFrame *frame = new MainFrame( _("Hello World"), wxPoint(50, 50),  wxSize(450,340) );
    frame->Show(true);
    SetTopWindow(frame);
    return true;
}

MainFrame::MainFrame(const wxString& title, const wxPoint& pos, const wxSize& size)
    : wxFrame( NULL, -1, title, pos, size )
{
    wxMenu *menuFile = new wxMenu;

    menuFile->Append( ID_About, _("&About...") );
    menuFile->AppendSeparator();
    menuFile->Append( ID_Quit, _("E&xit") );

    wxMenuBar *menuBar = new wxMenuBar;
    menuBar->Append( menuFile, _("&File") );

    this->SetMenuBar( menuBar );

    CreateStatusBar();
    SetStatusText( _("Welcome to wxWidgets!") );
}

void MainFrame::OnQuit(wxCommandEvent& WXUNUSED(event)) {
    Close(TRUE);
}

void MainFrame::OnAbout(wxCommandEvent& WXUNUSED(event)) {
    wxMessageBox(
        _("This is a wxWidgets Hello world sample"),
        _("About Hello World"),
        wxOK | wxICON_INFORMATION, this
    );
}

