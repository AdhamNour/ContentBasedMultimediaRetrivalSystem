import 'package:flutter/material.dart';

class SearchScreen extends StatelessWidget {
  static const routeName = 'SEARCH_SCREEN';

  @override
  Widget build(BuildContext context) {
  final args = ModalRoute.of(context)!.settings.arguments as String;

    return Container(
      child: Text('this is the ${args} screen'),
    );
  }
}
