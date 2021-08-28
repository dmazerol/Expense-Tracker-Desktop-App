#include "add_user.h"
#include "ui_add_user.h"

add_user::add_user(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::add_user)
{
    ui->setupUi(this);
}

add_user::~add_user()
{
    delete ui;
}
