#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_pushButton_clicked()
{
    QString doll = ui->lineEdit->text();
//    QString tk = ui->lineEdit_2->text();
    QString rat = ui->lineEdit_3->text();
    float d = doll.toFloat();
//    float t = tk.toFloat();
    float r = rat.toFloat();
float t = d * r;
ui->lineEdit_2->setText(QString::number(t) );
}

void MainWindow::on_pushButton_2_clicked()
{
//    QString doll = ui->lineEdit->text();
    QString tk = ui->lineEdit_2->text();
    QString rat = ui->lineEdit_3->text();
//    float d = doll.toFloat();
    float t = tk.toFloat();
    float r = rat.toFloat();
float d = t / r;
ui->lineEdit->setText(QString::number(d) );

}
