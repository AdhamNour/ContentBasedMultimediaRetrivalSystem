import 'package:cached_network_image/cached_network_image.dart';
import 'package:flutter/material.dart';
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
      itemBuilder: (_, index) => Padding(
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
                      placeholder: (context, url) =>
                          CircularProgressIndicator(),
                      errorWidget: (context, url, error) => Icon(Icons.error),
                    )
                  : YoutubePlayer(controller: _controller),
            ],
          ),
        )),
      ),
      itemCount: 10,
    ));
  }
}
