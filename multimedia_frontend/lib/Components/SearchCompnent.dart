import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'package:provider/provider.dart';
import 'package:http/http.dart' as http;

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

  void searchRequest(ResultsProvider resultProvider, {String? url}) {
    print('[AdhamNour/searchRequest]${url}');
    http.post(Uri.parse('http://192.168.1.9:5000/${widget.searchType}'), body: {
      'link': url,
      'retreival_algorithms': jsonEncode(algorithms)
    }).then((value) {
      var x = jsonDecode(value.body)['result_links'];
      List<String> xx = [];
      for (int i = 0; i < x.length; i++) {
        // print(x[i]['link']);

        xx.add(x[i].toString());
      }
      resultProvider.results = xx;
    });
  }

  @override
  Widget build(BuildContext context) {
    final screenSize = MediaQuery.of(context).size;
    final resultProvider = Provider.of<ResultsProvider>(context);
    final urlController = TextEditingController();
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
                      controller: urlController,
                    ),
                  ),
                  IconButton(
                      onPressed: () {
                        print("[AdhamNour]${urlController.text}");
                        searchRequest(resultProvider, url: urlController.text);
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
                            searchRequest(resultProvider,
                                url: urlController.text);
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
