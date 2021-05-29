import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'package:provider/provider.dart';

import '../providers/ResultProvider.dart';

class SearchComponent extends StatefulWidget {
  final String searchType;
  SearchComponent({this.searchType = 'error'});

  @override
  _SearchComponentState createState() => _SearchComponentState();
}

class _SearchComponentState extends State<SearchComponent> {
  var algorithms = {
    'Histogram': false,
    'Text': true,
    'GaborFilter': true,
    'RESNET': false
  };
  @override
  Widget build(BuildContext context) {
    var screenSize = MediaQuery.of(context).size;
    final resultProvider = Provider.of<ResultsProvider>(context);
    return Card(
      child: Column(
        children: [
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Container(
              child: Row(
                children: [
                  //checkboxes in images only
                  Expanded(
                    child: TextField(
                      decoration: InputDecoration(
                          border: OutlineInputBorder(),
                          hintText: '${widget.searchType} URL'),
                    ),
                  ),
                  IconButton(
                      onPressed: () => {
                            resultProvider.results = [
                              'https://youtu.be/mTCESSzPZSw'
                            ]
                            //TODO: fix this to send http request instead
                          },
                      icon: FaIcon(FontAwesomeIcons.search))
                ],
              ),
            ),
          ),
          Padding(
            //Add Camera Button
            padding: const EdgeInsets.all(8.0),
            child: ElevatedButton.icon(
                onPressed: () => {},
                icon: FaIcon(FontAwesomeIcons.handsHelping),
                label: Text('Helping ${widget.searchType}')),
          ),
          if (widget.searchType == 'Image')
            Padding(
              //Add Camera Button
              padding: const EdgeInsets.all(8.0),
              child: Container(
                child: ListView(
                  children: algorithms.keys
                      .map((e) => CheckboxListTile(
                          value: algorithms[e],
                          onChanged: (newVal) {
                            resultProvider.results = [
                              ...resultProvider.results,
                              'https://images5.alphacoders.com/903/903845.png'
                            ]; //TODO: fix it with sending an HTTP request to server
                            setState(() {
                              if (newVal != null) {
                                algorithms[e] = newVal ? true : false;
                              }
                            });
                          },
                          title: Text(e)))
                      .toList(),
                ),
                height: screenSize.height * 0.185,
              ),
            )
        ],
      ),
    );
  }
}
