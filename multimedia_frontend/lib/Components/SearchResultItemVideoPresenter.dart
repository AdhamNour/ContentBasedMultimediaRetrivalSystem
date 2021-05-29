import 'package:flutter/material.dart';
import 'package:youtube_player_flutter/youtube_player_flutter.dart';

class SearchResultItemVideoPresenter extends StatelessWidget {
  final url;
  SearchResultItemVideoPresenter({this.url});
  @override
  Widget build(BuildContext context) {
    YoutubePlayerController _controller = YoutubePlayerController(
      initialVideoId: YoutubePlayer.convertUrlToId(url).toString(),
      flags: YoutubePlayerFlags(
        autoPlay: false,
        mute: false,
      ),
    );
    return YoutubePlayer(controller: _controller);
  }
}
