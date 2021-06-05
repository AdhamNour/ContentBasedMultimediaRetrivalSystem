import 'package:cached_network_image/cached_network_image.dart';
import 'package:flutter/material.dart';
import 'package:multimedia_frontend/Components/SearchResultItem.dart';
import 'package:multimedia_frontend/providers/ResultProvider.dart';
import 'package:provider/provider.dart';
import 'package:youtube_player_flutter/youtube_player_flutter.dart';

class SearchResultsListView extends StatelessWidget {
  final searchType;
  SearchResultsListView({this.searchType});
  @override
  Widget build(BuildContext context) {
    final resultProvider = Provider.of<ResultsProvider>(context).results;
    return resultProvider.length > 0
        ? ListView.builder(
            itemBuilder: (_, index) => SearchResultItem(
              searchType: searchType,
              index: index,url: resultProvider[index]["url"], Similarity: resultProvider[index]['Similarity'],
            ),
            itemCount: resultProvider.length,
          )
        : Center(
            child: Text('search it'),
          );
  }
}
