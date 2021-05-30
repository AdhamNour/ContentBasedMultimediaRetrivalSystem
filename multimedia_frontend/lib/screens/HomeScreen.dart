import 'dart:io';

import 'package:file_picker/file_picker.dart';
import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import './SearchScreen.dart';

class HomeScreen extends StatelessWidget {
  static const String routeName = "home";

  void showSummary(FilePickerResult? result, BuildContext context) {
    if (result != null) {
      File file = File(result.files.single.path.toString());
      showDialog(
          context: context,
          builder: (ctx) => AlertDialog(
                title: Text("Confirm Image"),
                content: Column(
                  mainAxisSize: MainAxisSize.min,
                  children: [Text('you have selected'), Image.file(file)],
                ),
                actions: [
                  TextButton.icon(
                      onPressed: () {
                        Navigator.of(context).pop('ok');
                      },
                      icon: Icon(Icons.thumb_up),
                      label: Text('Okay'))
                ],
              )).then((value) {
        if (value != 'ok') {
          showDialog(
              context: context,
              builder: (ctx) => AlertDialog(
                    title: Text("Selection Canceled"),
                    content: Text("You have canceled the file selection"),
                  ));
        }
      });
    } else {
      // User canceled the picker
      showDialog(
          context: context,
          builder: (ctx) => AlertDialog(
                title: Text("Selection Canceled"),
                content: Text("You have canceled the file selection"),
              ));
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Contest Based Multimedia Retrival systems'),
      ),
      body: Center(
        child: Column(
          children: [
            Row(
              children: [
                ElevatedButton.icon(
                    onPressed: () => {
                          Navigator.of(context).pushNamed(
                              SearchScreen.routeName,
                              arguments: 'Video')
                        },
                    icon: FaIcon(FontAwesomeIcons.video),
                    label: Text('Video')),
                TextButton.icon(
                    onPressed: () => {
                          Navigator.of(context).pushNamed(
                              SearchScreen.routeName,
                              arguments: 'Image')
                        },
                    icon: FaIcon(FontAwesomeIcons.image),
                    label: Text('Image'))
              ],
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            ),
            Row(
              children: [
                TextButton.icon(
                    onPressed: () async {
                      FilePickerResult? result =
                          await FilePicker.platform.pickFiles();
                      showSummary(result, context);
                    },
                    icon: FaIcon(FontAwesomeIcons.fileVideo),
                    label: Text('Upload Video')),
                ElevatedButton.icon(
                    onPressed: () async {
                      FilePickerResult? result =
                          await FilePicker.platform.pickFiles();
                      showSummary(result, context);
                    },
                    icon: FaIcon(FontAwesomeIcons.images),
                    label: Text('Upload Image')),
              ],
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            )
          ],
          mainAxisSize: MainAxisSize.min,
        ),
      ),
    );
  }
}
