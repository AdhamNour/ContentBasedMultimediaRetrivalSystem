import 'package:cached_network_image/cached_network_image.dart';
import 'package:flutter/material.dart';
import 'package:multimedia_frontend/Components/SearchResultItem.dart';
import 'package:youtube_player_flutter/youtube_player_flutter.dart';

class SearchResultsListView extends StatelessWidget {
  final searchType;
  SearchResultsListView({this.searchType});
  @override
  Widget build(BuildContext context) {
    YoutubePlayerController _controller = YoutubePlayerController(
      initialVideoId: YoutubePlayer.convertUrlToId(
              'https://youtu.be/E_q9maUnWes?list=PLaUMIRsX73gLp_2JqaB51MICkUfsHsdEi')
          .toString(),
      flags: YoutubePlayerFlags(
        autoPlay: false,
        mute: true,
      ),
    );
    return Container(
        child: ListView.builder(
      itemBuilder: (_, index) => SearchResultItem(
        searchType: searchType,
        index: index,
      ),
      itemCount: 10,
    ));
  }
}
