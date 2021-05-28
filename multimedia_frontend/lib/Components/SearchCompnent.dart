import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';

class SearchComponent extends StatefulWidget {
  final String searchType;
  SearchComponent({this.searchType = 'error'});

  @override
  _SearchComponentState createState() => _SearchComponentState();
}

class _SearchComponentState extends State<SearchComponent> {
  var algorithms = {'Histogram': false, 'Text': true};
  @override
  Widget build(BuildContext context) {
    var screenSize = MediaQuery.of(context).size;
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
                      onPressed: () => {},
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
                            setState(() {
                              if (newVal != null) {
                                algorithms[e] = newVal ? true : false;
                              }
                            });
                          },
                          title: Text(e)))
                      .toList(),
                ),
                height: screenSize.height*0.15,
              ),
            )
        ],
      ),
    );
  }
}
