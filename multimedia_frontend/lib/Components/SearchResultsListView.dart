import 'package:cached_network_image/cached_network_image.dart';
import 'package:flutter/material.dart';

class SearchResultsListView extends StatelessWidget {
  final searchType;
  SearchResultsListView({this.searchType});
  @override
  Widget build(BuildContext context) {
    return Container(
        child: ListView.builder(
      itemBuilder: (_, index) => Padding(
        padding: const EdgeInsets.all(8.0),
        child: Card(
            child: Padding(
          padding: const EdgeInsets.all(8.0),
          child: Column(
            children: [
              Text('result #${index+1}'),
              CachedNetworkImage(
                imageUrl: "https://images6.alphacoders.com/345/thumb-1920-345153.jpg",
                placeholder: (context, url) => CircularProgressIndicator(),
                errorWidget: (context, url, error) => Icon(Icons.error),
              ),
            ],
          ),
        )),
      ),
      itemCount: 10,
    ));
  }
}
