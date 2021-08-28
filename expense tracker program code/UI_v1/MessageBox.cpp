#include "MessageBox.h"
#include "ui_errorbox.h"

errorBox::errorBox(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::errorBox)
{
    ui->setupUi(this);
}

errorBox::~errorBox()
{
    delete ui;
}
