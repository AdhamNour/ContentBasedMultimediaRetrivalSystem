import 'package:flutter/material.dart';
import 'package:multimedia_frontend/Components/ImageCompnent.dart';
import 'package:multimedia_frontend/Components/VideoComponent.dart';

class SearchScreen extends StatelessWidget {
  static const routeName = 'SEARCH_SCREEN';

  @override
  Widget build(BuildContext context) {
    final args = ModalRoute.of(context)!.settings.arguments as String;
    Widget renderElement = VideoRetrivalComponent();
    if (args == 'Image') {
      renderElement = ImageRetrivalComponent();
    }
    return Scaffold(
        appBar: AppBar(
          title: Text('Content Based $args Retrival System'),
        ),
        body: Column(
          children: [
            renderElement,
            Expanded(
              child: Center(child: Text('result area')),
            )
          ],
        ));
  }
}
