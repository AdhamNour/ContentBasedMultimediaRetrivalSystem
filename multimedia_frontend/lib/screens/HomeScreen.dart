import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
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
            ElevatedButton.icon(
                onPressed: () => {
                      Navigator.of(context)
                          .pushNamed(SearchScreen.routeName, arguments: 'Video')
                    },
                icon: FaIcon(FontAwesomeIcons.video),
                label: Text('Video')),
            TextButton.icon(
                onPressed: () => {
                      Navigator.of(context)
                          .pushNamed(SearchScreen.routeName, arguments: 'Image')
                    },
                icon: FaIcon(FontAwesomeIcons.image),
                label: Text('Image'))
          ],
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        ),
      ),
    );
  }
}
