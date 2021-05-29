import 'package:flutter/material.dart';
import 'package:multimedia_frontend/Components/SearchCompnent.dart';
import 'package:multimedia_frontend/Components/SearchResultsListView.dart';
import 'package:multimedia_frontend/providers/ResultProvider.dart';
import 'package:provider/provider.dart';

class SearchScreen extends StatelessWidget {
  static const routeName = 'SEARCH_SCREEN';

  @override
  Widget build(BuildContext context) {
    final args = ModalRoute.of(context)!.settings.arguments as String;

    return Scaffold(
        appBar: AppBar(
          title: Text('Content Based $args Retrival System'),
        ),
        body: ChangeNotifierProvider(
          create: (_) => ResultsProvider(),
          child: Column(
            children: [
              SearchComponent(
                searchType: args,
              ),
              Expanded(
                  child: SearchResultsListView(
                searchType: args,
              ))
            ],
          ),
        ));
  }
}
