/********************************************************************************
** Form generated from reading UI file 'frmmain.ui'
**
** Created by: Qt User Interface Compiler version 5.11.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef FRMMAIN_H
#define FRMMAIN_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QFrame>
#include <QtWidgets/QLabel>
#include <QtWidgets/QListView>
#include <QtWidgets/QPushButton>

QT_BEGIN_NAMESPACE

class Ui_K8S
{
public:
    QAction *cboProjet;
    QLabel *lblProjet;
    QComboBox *cboProject;
    QLabel *lblcluster;
    QComboBox *cboK8S;
    QPushButton *btnAddCredentails;
    QPushButton *btnAddCredentails_2;
    QListView *listView;

    void setupUi(QFrame *K8S)
    {
        if (K8S->objectName().isEmpty())
            K8S->setObjectName(QStringLiteral("K8S"));
        K8S->resize(500, 284);
        cboProjet = new QAction(K8S);
        cboProjet->setObjectName(QStringLiteral("cboProjet"));
        lblProjet = new QLabel(K8S);
        lblProjet->setObjectName(QStringLiteral("lblProjet"));
        lblProjet->setGeometry(QRect(10, 10, 101, 16));
        cboProject = new QComboBox(K8S);
        cboProject->setObjectName(QStringLiteral("cboProject"));
        cboProject->setGeometry(QRect(120, 10, 211, 22));
        lblcluster = new QLabel(K8S);
        lblcluster->setObjectName(QStringLiteral("lblcluster"));
        lblcluster->setGeometry(QRect(10, 50, 101, 16));
        cboK8S = new QComboBox(K8S);
        cboK8S->setObjectName(QStringLiteral("cboK8S"));
        cboK8S->setGeometry(QRect(120, 50, 211, 22));
        btnAddCredentails = new QPushButton(K8S);
        btnAddCredentails->setObjectName(QStringLiteral("btnAddCredentails"));
        btnAddCredentails->setGeometry(QRect(120, 90, 101, 23));
        btnAddCredentails_2 = new QPushButton(K8S);
        btnAddCredentails_2->setObjectName(QStringLiteral("btnAddCredentails_2"));
        btnAddCredentails_2->setGeometry(QRect(240, 90, 101, 23));
        listView = new QListView(K8S);
        listView->setObjectName(QStringLiteral("listView"));
        listView->setGeometry(QRect(10, 130, 441, 111));

        retranslateUi(K8S);

        QMetaObject::connectSlotsByName(K8S);
    } // setupUi

    void retranslateUi(QFrame *K8S)
    {
        K8S->setWindowTitle(QApplication::translate("K8S", "Frame", nullptr));
        cboProjet->setText(QApplication::translate("K8S", "onselect", nullptr));
        lblProjet->setText(QApplication::translate("K8S", "Select GCP Project", nullptr));
        lblcluster->setText(QApplication::translate("K8S", "Select K8S Cluster", nullptr));
        btnAddCredentails->setText(QApplication::translate("K8S", "Get Credentials", nullptr));
        btnAddCredentails_2->setText(QApplication::translate("K8S", "Get Workloads", nullptr));
    } // retranslateUi

};

namespace Ui {
    class K8S: public Ui_K8S {};
} // namespace Ui

QT_END_NAMESPACE

#endif // FRMMAIN_H
