import 'package:flutter/material.dart';

import './SearchScreen.dart';

class HomeScreen extends StatelessWidget {
  static const String routeName = "home";
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Contest Based Multimedia Retrival systems'),
      ),
      body: Center(
        child: Row(
          children: [
            ElevatedButton(
                onPressed: () => {
                      Navigator.of(context)
                          .pushNamed(SearchScreen.routeName, arguments: 'Video')
                    },
                child: Text('Video')),
            TextButton(
                onPressed: () => {
                      Navigator.of(context)
                          .pushNamed(SearchScreen.routeName, arguments: 'Image')
                    },
                child: Text('Image'))
          ],
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        ),
      ),
    );
  }
}
