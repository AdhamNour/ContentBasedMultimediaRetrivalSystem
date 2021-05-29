import 'package:flutter/cupertino.dart';

class ResultsProvider extends ChangeNotifier {
  List<String> _results = [];

  List<String> get results {
    return [..._results];
  }

  void set results(List<String> iResults) {
    _results = iResults;
    notifyListeners();
  }
}
