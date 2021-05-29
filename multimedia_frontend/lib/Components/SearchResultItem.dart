import 'package:cached_network_image/cached_network_image.dart';
import 'package:flutter/material.dart';
import 'package:multimedia_frontend/Components/SearchResultItemVideoPresenter.dart';

class SearchResultItem extends StatelessWidget {
  final searchType,index;
  SearchResultItem({this.searchType,this.index});
  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: Card(
          child: Padding(
        padding: const EdgeInsets.all(8.0),
        child: Column(
          children: [
            Text('result #${index + 1}'),
            searchType == 'Image'
                ? CachedNetworkImage(
                    imageUrl:
                        "https://images6.alphacoders.com/345/thumb-1920-345153.jpg",
                    placeholder: (context, url) => CircularProgressIndicator(),
                    errorWidget: (context, url, error) => Icon(Icons.error),
                  )
                : SearchResultItemVideoPresenter(),
          ],
        ),
      )),
    );
  }
}
