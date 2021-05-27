import 'package:flutter/material.dart';
import 'package:multimedia_frontend/Components/SearchCompnent.dart';


class SearchScreen extends StatelessWidget {
  static const routeName = 'SEARCH_SCREEN';

  @override
  Widget build(BuildContext context) {
    final args = ModalRoute.of(context)!.settings.arguments as String;
   
    return Scaffold(
        appBar: AppBar(
          title: Text('Content Based $args Retrival System'),
        ),
        body: Column(
          children: [
            SearchComponent(searchType: args,),
            Expanded(
              child: Center(child: Text('result area')),
            )
          ],
        ));
  }
}
