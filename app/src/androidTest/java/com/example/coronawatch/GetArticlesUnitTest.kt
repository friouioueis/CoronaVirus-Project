package com.example.coronawatch

import junit.framework.Assert.assertEquals
import org.junit.Test

val dataString = "[{\"idArticle\":4,\"photos\":[{\"idPhoto\":8,\"lienPhAc\":\"http://96923c01d724.ngrok.io/media/article_images/sketch-effect-logo-mockup-base-.jpg\",\"idArticlePh\":4}],\"videos\":[],\"dateAr\":\"2020-04-24T21:40:45Z\",\"contenuAr\":\"<h1>HELLO</h1>\\r\\n<h2>hello</h2>\\r\\n<h3>hello</h3>\\r\\n<h4>hello</h4>\",\"terminerAR\":true,\"validerAR\":true,\"refuserAR\":true,\"idRedacteurAr\":1,\"redacteur_name\":\"admin\",\"idModerateurAr\":1,\"moderateur_name\":\"admin\"}]"
class GetArticlesUnitTest {
    @Test
    fun dataParsingTest(){
        assertEquals(4 , dataParsing(dataString , null))
    }
}