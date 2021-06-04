import 'dart:io';

import 'package:file_picker/file_picker.dart';
import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'package:http/http.dart' as http;

import 'package:multimedia_frontend/Components/SearchResultItemVideoPresenter.dart';
import './SearchScreen.dart';

class HomeScreen extends StatelessWidget {
  static const String routeName = "home";

  void showSummary(
      {FilePickerResult? result,
      required BuildContext context,
      required String type}) {
    if (result != null) {
      File file = File(result.files.single.path.toString());
      showDialog(
          context: context,
          builder: (ctx) {
            return AlertDialog(
              title: Text("Complete ${type} Data"),
              content: SingleChildScrollView(
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Text('you have selected'),
                    Image.file(file),
                    Padding(
                      padding: const EdgeInsets.all(8.0),
                      child: TextField(
                        decoration: InputDecoration(
                            border: OutlineInputBorder(), hintText: 'Author'),
                      ),
                    ),
                    Padding(
                      padding: const EdgeInsets.all(8.0),
                      child: TextField(
                        decoration: InputDecoration(
                            border: OutlineInputBorder(), hintText: 'Title'),
                      ),
                    ),
                    Padding(
                      padding: const EdgeInsets.all(8.0),
                      child: TextField(
                        decoration: InputDecoration(
                            border: OutlineInputBorder(),
                            hintText: 'Discription'),
                      ),
                    )
                  ],
                ),
              ),
              actions: [
                TextButton.icon(
                    onPressed: () {
                      Navigator.of(context).pop('ok');
                      var request = http.MultipartRequest('POST',
                          Uri.parse('http://192.168.1.9:5000/uploadBinaryImage'))..fields['hello']='hello';
                      print(file.readAsBytesSync());
                      print(http.MultipartFile.fromBytes(
                          'content', file.readAsBytesSync()).toString());
                      request.files.add(http.MultipartFile.fromBytes(
                          'content', file.readAsBytesSync(), filename: file.path.split('/').last));
                      request
                          .send()
                          .then((value) => print('[AdhamNour]${value.toString()}'));
                    },
                    icon: Icon(Icons.thumb_up),
                    label: Text('Okay'))
              ],
            );
          }).then((value) {
        if (value != 'ok') {
          showDialog(
              context: context,
              builder: (ctx) => AlertDialog(
                    title: Text("Selection Canceled"),
                    content: Text("You have canceled the file selection"),
                  ));
        }
      });
    } else if (type == 'Video') {
      showDialog(
          context: context,
          builder: (ctx) {
            final urlController = TextEditingController();
            return AlertDialog(
              title: Text("Complete ${type} Data"),
              content: SingleChildScrollView(
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    VideoPreview(
                      urlController: urlController,
                    ),
                    Padding(
                      padding: const EdgeInsets.all(8.0),
                      child: TextField(
                        decoration: InputDecoration(
                            border: OutlineInputBorder(), hintText: 'Author'),
                      ),
                    ),
                  ],
                ),
              ),
              actions: [
                TextButton.icon(
                    onPressed: () {
                      Navigator.of(context).pop('ok');
                    },
                    icon: Icon(Icons.thumb_up),
                    label: Text('Okay'))
              ],
            );
          }).then((value) {
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
                      showSummary(context: context, type: 'Video');
                    },
                    icon: FaIcon(FontAwesomeIcons.fileVideo),
                    label: Text('Upload Video')),
                ElevatedButton.icon(
                    onPressed: () async {
                      FilePickerResult? result =
                          await FilePicker.platform.pickFiles();
                      showSummary(
                          result: result, context: context, type: 'Image');
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

class VideoPreview extends StatefulWidget {
  final TextEditingController urlController;

  const VideoPreview({
    Key? key,
    required this.urlController,
  }) : super(key: key);

  @override
  _VideoPreviewState createState() => _VideoPreviewState();
}

class _VideoPreviewState extends State<VideoPreview> {
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Padding(
          padding: const EdgeInsets.all(8.0),
          child: Row(
            children: [
              Expanded(
                child: Padding(
                  padding: const EdgeInsets.all(8.0),
                  child: TextField(
                    decoration: InputDecoration(
                        border: OutlineInputBorder(),
                        hintText: 'Youtube Video URL'),
                    controller: widget.urlController,
                  ),
                ),
              ),
              IconButton(
                  onPressed: () => setState(() {}),
                  icon: FaIcon(FontAwesomeIcons.search))
            ],
          ),
        ),
        if (widget.urlController.text.isNotEmpty)
          SearchResultItemVideoPresenter(url: widget.urlController.text)
      ],
    );
  }
}
