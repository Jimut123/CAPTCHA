#include "dialog.h"
#include "ui_dialog.h"
#include <QPainterPath>
#include <QPainter>
#include <QtMath>

Dialog::Dialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Dialog)
{
    ui->setupUi(this);
}

Dialog::~Dialog()
{
    delete ui;
}


void Dialog::paintEvent(QPaintEvent *)
{
    QPainter painter(this);
	Captcha cp;
	cp.randomize();
    cp.setDifficulty(3);
	/*cp.loadDictionary("dictionary.txt");
	cp.setTextGeneration(Captcha::TextGeneration_Dictionary);*/
	cp.generateText();
	painter.drawImage(30, 30, cp.captchaImage());
}
