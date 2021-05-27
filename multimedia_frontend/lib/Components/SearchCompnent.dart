import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';

class SearchComponent extends StatelessWidget {
  final String searchType;
  SearchComponent({this.searchType='error'});
  @override
  Widget build(BuildContext context) {
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
                          border: OutlineInputBorder(), hintText: '${searchType} URL'),
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
                label: Text('Helping $searchType')),
          )
        ],
      ),
    );
  }
}
