import 'package:flutter/material.dart';
import './screens/HomeScreen.dart';
import 'screens/SearchScreen.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Content Based Multimedia Retrival System',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: HomeScreen(),
      routes: {
        HomeScreen.routeName: (ctx) => HomeScreen(),
        SearchScreen.routeName: (ctx) => SearchScreen(),
      },
    );
  }
}
