#ifndef MESSAGEBOX_H
#define MESSAGEBOX_H

#include <QDialog>

namespace Ui {
class errorBox;
}

class errorBox : public QDialog
{
    Q_OBJECT

public:
    explicit errorBox(QWidget *parent = nullptr);
    ~errorBox();

private:
    Ui::errorBox *ui;
};

#endif // MESSAGEBOX_H
