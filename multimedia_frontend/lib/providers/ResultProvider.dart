import 'package:flutter/cupertino.dart';

class ResultsProvider extends ChangeNotifier {
  List _results = [];

  List get results {
    return [..._results];
  }

  void set results(List iResults) {
    _results = iResults;
    notifyListeners();
  }
}
