@file:Suppress("UNCHECKED_CAST")

package com.example.coronawatch

import android.content.Context
import androidx.appcompat.app.AppCompatActivity
import java.io.*

object ReadWriteFileManager {

    fun readFile(contect : Context) : ArrayList<Wilaya>{
        val fileName = "contact.txt"
        try {
            val fis: FileInputStream = contect.openFileInput(fileName)
            var iss = ObjectInputStream(fis)
            val interventions: ArrayList<Wilaya> = iss.readObject() as ArrayList<Wilaya>
            iss.close()
            fis.close()
            return interventions
        }catch (e : FileNotFoundException){
            println("file not found")
        }


        return arrayListOf<Wilaya>()
    }


    fun writeFile(contect : Context, wilayaList:ArrayList<Wilaya>){



        val fileName = "contact.txt"
        val fos: FileOutputStream = contect.openFileOutput(fileName, AppCompatActivity.MODE_PRIVATE)
        val os = ObjectOutputStream(fos)
        os.writeObject(wilayaList)
        os.close()
        fos.close()


    }



    fun writeWilaya(nContext : Context) {
        val listWilaya = arrayListOf<Wilaya>()
        listWilaya.add(Wilaya(1, "Adrar", 27.875179, -0.295720))
        listWilaya.add(Wilaya(2, "Chlef", 36.154816, 1.325696))
        listWilaya.add(Wilaya(3, "Laghouat", 33.800010, 2.890250))
        listWilaya.add(Wilaya(4, "Oum El Bouaghi", 35.876549, 7.115390))
        listWilaya.add(Wilaya(5, "Batna", 35.3384291, 5.7315453))
        listWilaya.add(Wilaya(6, "Bejaia", 36.7511783, 5.0643687))
        listWilaya.add(Wilaya(7, "Biskra", 34.320341, 4.7246792))
        listWilaya.add(Wilaya(8, "Béchar", 31.385726, -2.0115958))
        listWilaya.add(Wilaya(9, "Blida", 36.4701645, 2.8287985))
        listWilaya.add(Wilaya(10, "Bouira", 36.2316481, 3.9082579))
        listWilaya.add(Wilaya(11, "Tamanrasset", 24.3753438, 4.3208436))
        listWilaya.add(Wilaya(12, "Tébessa", 35.124945, 7.9011735))
        listWilaya.add(Wilaya(13, "Tlemcen", 34.881789, -1.316699))
        listWilaya.add(Wilaya(14, "Tiaret", 34.8947575, 1.5945792))
        listWilaya.add(Wilaya(15, "Tizi Ouzou", 36.6816175, 4.237186))
        listWilaya.add(Wilaya(16, "Alger", 36.7753606, 3.0601882))
        listWilaya.add(Wilaya(17, "Djelfa", 34.342841, 3.2172531))
        listWilaya.add(Wilaya(18, "Jijel", 36.7292188, 5.9607776))
        listWilaya.add(Wilaya(19, "Sétif", 36.1892751, 5.403493))
        listWilaya.add(Wilaya(20, "Saïda", 34.743349, 0.2440764))
        listWilaya.add(Wilaya(21, "Skikda", 36.7545115, 6.8856255))
        listWilaya.add(Wilaya(22, "Sidi Bel Abbès", 34.682268, -0.4357555))
        listWilaya.add(Wilaya(23, "Annaba", 36.8982165, 7.7549272))
        listWilaya.add(Wilaya(24, "Guelma", 36.3491635, 7.409499))
        listWilaya.add(Wilaya(25, "Constantine", 36.364519, 6.60826))
        listWilaya.add(Wilaya(26, "Médéa", 35.9752045, 3.0123504))
        listWilaya.add(Wilaya(27, "Mostaganem", 36.0026915, 0.3686867))
        listWilaya.add(Wilaya(28, "M'Sila", 35.1300205, 4.2003107))
        listWilaya.add(Wilaya(29, "Mascara", 35.3978385, 0.2430195))
        listWilaya.add(Wilaya(30, "Ouargla", 30.9980145, 6.7664536))
        listWilaya.add(Wilaya(31, "Oran", 35.7032751, -0.6492976))
        listWilaya.add(Wilaya(32, "El Bayadh", 32.570303, 1.1259581))
        listWilaya.add(Wilaya(33, "Illizi", 27.8528505, 7.8189636))
        listWilaya.add(Wilaya(34, "Bordj Bou Arreridj", 36.095506, 4.6611002))
        listWilaya.add(Wilaya(35, "Boumerdès", 36.7358032, 3.6163046))
        listWilaya.add(Wilaya(36, "El Tarf", 36.6713563, 8.070134))
        listWilaya.add(Wilaya(37, "Tindouf", 27.543907, -6.2400539))
        listWilaya.add(Wilaya(38, "Tissemsilt", 35.7858975, 1.8340957))
        listWilaya.add(Wilaya(39, "El Oued", 33.215441, 7.1553214))
        listWilaya.add(Wilaya(40, "Khenchela", 34.9133455, 6.9059431))
        listWilaya.add(Wilaya(41, "Souk Ahras", 36.1378681, 7.8262426))
        listWilaya.add(Wilaya(42, "Tipaza", 36.5272741, 2.1683687))
        listWilaya.add(Wilaya(43, "Mila", 36.2502135, 6.1652163))
        listWilaya.add(Wilaya(44, "Aïn Defla", 36.1586843, 2.0842817))
        listWilaya.add(Wilaya(45, "Naâma", 33.2336851, -0.8151958))
        listWilaya.add(Wilaya(46, "Aïn Témouchent", 35.3650471, -0.9452807))
        listWilaya.add(Wilaya(47, "Ghardaïa", 32.440827, 3.5618209))
        listWilaya.add(Wilaya(48, "Relizane", 35.8363185, 0.9118537))
        ReadWriteFileManager.writeFile(nContext , listWilaya)

    }
}