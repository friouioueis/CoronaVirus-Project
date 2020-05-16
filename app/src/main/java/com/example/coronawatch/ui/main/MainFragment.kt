package com.example.coronawatch.ui.main

import android.annotation.SuppressLint
import android.content.ContentValues.TAG
import android.content.Context
import android.content.res.Resources
import android.graphics.Bitmap
import android.graphics.Canvas
import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.core.content.ContextCompat
import androidx.fragment.app.Fragment
import androidx.lifecycle.ViewModelProviders
import com.example.coronawatch.R
import com.example.coronawatch.ReadWriteFileManager
import com.example.coronawatch.Wilaya
import com.google.android.gms.maps.*
import com.google.android.gms.maps.model.*


@Suppress("CAST_NEVER_SUCCEEDS")
class MainFragment : Fragment() {

    lateinit var map: SupportMapFragment
    private lateinit var googleMap: GoogleMap
    private lateinit var mainViewModel: MainViewModel
    private var mMap: GoogleMap? = null

    @SuppressLint("WrongViewCast")
    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        mainViewModel =
            ViewModelProviders.of(this).get(MainViewModel::class.java)
        val root = inflater.inflate(R.layout.fragment_main, container, false)


        //map = activity?.supportFragmentManager?.findFragmentById(R.id.map_fragment) as SupportMapFragment
        /* (activity?.supportFragmentManager?.findFragmentById(R.id.map_fragment) as SupportMapFragment?)?.let {
              it.getMapAsync(OnMapReadyCallback { it ->
                  googleMap = it
                  googleMap.mapType = GoogleMap.MAP_TYPE_NORMAL
                  googleMap.setMaxZoomPreference(8.0F)
                  googleMap.setMinZoomPreference(3.0F)
                  googleMap.uiSettings.isRotateGesturesEnabled = false
                  var location1 = LatLng(13.03 , 77.60)
                  googleMap.addMarker(MarkerOptions().position(location1).title("location1"))
                  setMapStyle(googleMap)

                  true

              })
          }*/

/*
        val fragment = MapsFragment()
        val fragmentTransaction: androidx.fragment.app.FragmentTransaction? =
            activity?.supportFragmentManager?.beginTransaction()
        fragmentTransaction?.replace(R.id.map_fragment, fragment)
        fragmentTransaction?.commit()
        fragment.getMapAsync(OnMapReadyCallback {
            googleMap = it
            onMapReady(googleMap)
        })*/






        return root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        val listWilaya = context?.let { ReadWriteFileManager.readFile(it) }
        val fragmentManager = activity?.supportFragmentManager
        val fragmentTransaction = fragmentManager?.beginTransaction()
        val fragment = SupportMapFragment()
        fragmentTransaction?.replace(R.id.map_fragment, fragment)
        fragmentTransaction?.commit()
        println("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
        fragment.getMapAsync(OnMapReadyCallback { googleMap ->
            googleMap.mapType = GoogleMap.MAP_TYPE_NORMAL
            googleMap.setMaxZoomPreference(7.5F)
            googleMap.setMinZoomPreference(6.0F)
            googleMap.uiSettings.isRotateGesturesEnabled = false
            var location = LatLng(13.03, 77.60)
            googleMap.addMarker(MarkerOptions().position(location).title("location1"))
            setMapStyle(googleMap)

            listWilaya?.forEach {
                location = LatLng(it.latitude, it.longitude)
                googleMap.addMarker(
                    MarkerOptions().position(location).title(it.nom).icon(
                        context?.let { it1 -> bitmapDescriptorFromVector(it1, R.drawable.ic_fiber_manual_record_black_24dp) }
                    )
                )
            }

            val bounds = LatLngBounds(
                LatLng(22.188810256559687, -4.653530076146126),
                LatLng(36.23320965502827, 8.012905769050121)
            )
            googleMap.setLatLngBoundsForCameraTarget(bounds)

        })


        /* (activity?.supportFragmentManager?.findFragmentById(R.id.map_fragment) as SupportMapFragment?)?.let {
             map = it


         }*/
    }


    //map Style
    private fun setMapStyle(map: GoogleMap) {
        try {
            // Customize the styling of the base map using a JSON object defined
            // in a raw resource file.
            val success = map.setMapStyle(
                MapStyleOptions.loadRawResourceStyle(
                    context,
                    R.raw.map_style
                )
            )

            if (!success) {
                Log.e(TAG, "Style parsing failed.")
            }
        } catch (e: Resources.NotFoundException) {
            Log.e(TAG, "Can't find style. Error: ", e)
        }
    }

    /*override fun onMapReady(googleMap: GoogleMap) {
        try {
            val success = googleMap.setMapStyle(
                MapStyleOptions.loadRawResourceStyle(
                    context, R.raw.map_style
                )
            )
            if (!success) {
                println("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
            }
        } catch (e: Resources.NotFoundException) {
            Log.e(TAG, "Can't find style. Error: ", e)
        }
    }
*/

    private fun bitmapDescriptorFromVector(
        context: Context,
        vectorResId: Int
    ): BitmapDescriptor? {
        val vectorDrawable = ContextCompat.getDrawable(context, vectorResId)
        vectorDrawable!!.setBounds(
            0,
            0,
            vectorDrawable.intrinsicWidth,
            vectorDrawable.intrinsicHeight
        )
        val bitmap = Bitmap.createBitmap(
            vectorDrawable.intrinsicWidth,
            vectorDrawable.intrinsicHeight,
            Bitmap.Config.ARGB_8888
        )
        val canvas = Canvas(bitmap)
        vectorDrawable.draw(canvas)
        return BitmapDescriptorFactory.fromBitmap(bitmap)
    }

}
