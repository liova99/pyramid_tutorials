.. Pyramid Tutorials

.. _pyramid-tutorials:

======================
Pyramid チュートリアル
======================

.. This is the home of tutorial and patterns content for the Pyramid web
.. framework.

これは、 Pyramid ウェブフレームワークのチュートリアルとパターンコンテンツ
のホームです。


.. Available Pyramid tutorials

---------------------------------
利用可能な Pyramid チュートリアル
---------------------------------

.. Several Pyramid tutorials exist. Some are part of the main
.. `Pyramid Documentation`_, some are in this `Pyramid Tutorials`_
.. community project, and others are published elsewhere.

Pyramid のチュートリアルはいくつか存在します。あるものはメインの
`Pyramid Documentation`_ の一部です。あるものはこの `Pyramid
Tutorials`_ コミュニティープロジェクトにあります。また、別の場所で公開
されているものもあります。


.. .. _Pyramid Documentation: http://docs.pylonsproject.org/en/latest/docs/pyramid.html
.. .. _Pyramid Tutorials: http://docs.pylonsproject.org/projects/pyramid/en/1.4-branch/#tutorials

.. _Pyramid Documentation: http://docs.pylonsproject.jp/en/latest/docs/pyramid.html
.. _Pyramid Tutorials: http://docs.pylonsproject.jp/projects/pyramid-doc-ja/en/1.4-branch-doc-ja/#id3


.. These are the Pyramid tutorials we could locate during the PyCon USA sprints in March, 2013.

これらは 2013年3月に PyCon USA スプリントの間に確認できた Pyramid
チュートリアルです。


.. **ET** is the estimated time to complete each tutorial.

**ET** はそれぞれのチュートリアルを完成するまでの予想時間です。


.. ================== === ======================= =============================== ==================== ===============
.. name/link          ET* title                   description                     code repo            features
.. ================== === ======================= =============================== ==================== ===============
.. `firstapp`_        1h  Creating Your First     chapter 4 in the
..                        Pyramid Application     `Narrative Documentation`_ part `pyramid`_           * URL dispatch
..                                                of the main Pyramid docs

.. `wiki`_            4h  ZODB + Traversal Wiki   chapter 37 in the `Tutorials`_  `pyramid`_           * traversal
..                        Tutorial                part of the main Pyramid docs                        * ZODB

.. `wiki2`_           4h  SQLAlchemy + URL        chapter 38 in the `Tutorials`_  `pyramid`_           * URL dispatch
..                        Dispatch Wiki Tutorial  part of the main Pyramid docs                        * SQLAlchemy

.. `single_file`_     ?   Todo List Application   very short; a.k.a. The Single   `pyramid_tutorials`_
..                        in One File             ``tasks`` Tutorial              (this site)

.. `humans`_          12h Pyramid for Plone       Pyramid for Plone Developers    `pyramid_tutorials`_
..                        Developers                                              (this site)

.. `getting_started`_ 5h  Getting Started with    Presented by Paul Everitt at    `pyramid_tutorials`_ * URL dispatch
..                        Pyramid                 PyCon USA 2013                  (this site)          * SQLAlchemy
..                                                                                                     * Chameleon
..                                                                                                     * security

.. `blogr`_           4h  ``pyramid_blogr``       inspired by Flaskr app from the `pyramid_blogr`_     * URL dispatch
..                        Tutorial                Flask Web Framework Tutorial                         * SQLAlchemy
..                                                                                                     * Mako
..                                                                                                     * security
..                                                                                                     * WTForms
..                                                                                                     * pagination
.. `birdie`_          4h  Birdie Tutorial: a      presented by Carlos de la
..                        simple Twitter clone    Guardia at OSCON 2011 and PyCon `cguardia_tut`_
..                                                USA 2012
.. ================== === ======================= =============================== ==================== ===============


.. list-table::
   :header-rows: 1

   * - 名称/リンク
     - ET*
     - タイトル
     - 説明
     - リポジトリ
     - 機能

   * - `firstapp`_ (英語)
     - 1h
     - 最初の Pyramid アプリケーションの作成
     - メイン Pyramid ドキュメントの第4章 `Narrative Documentation`_
     - `pyramid`_
     - * URL dispatch
   * - `wiki`_ (英語)
     - 4h
     - ZODB + Traversal Wiki チュートリアル
     - メイン Pyramid ドキュメントの第37章 `Tutorials`_
     - `pyramid`_
     - * traversal
       * ZODB
   * - `wiki2`_
     - 4h
     - SQLAlchemy + URL ディスパッチ Wiki チュートリアル
     - メイン Pyramid ドキュメントの第38章 `Tutorials`_
     - `pyramid`_
     - * URL dispatch
       * SQLAlchemy
   * - `single_file`_ (英語)
     - ?
     - 単一ファイルの Todo List アプリケーション
     - 非常に短い; 別名 Single ``tasks`` チュートリアル
     - `pyramid_tutorials`_ (このサイト)
     -
   * - `humans`_ (英語)
     - 12h
     - Plone 開発者のための Pyramid
     - Plone 開発者のための Pyramid
     - `pyramid_tutorials`_ (このサイト)
     -
   * - `getting_started`_ (英語)
     - 5h
     - Pyramid を始める
     - PyCon USA 2013 で Paul Everitt によって発表された
     - `pyramid_tutorials`_ (このサイト)
     - * URL dispatch
       * SQLAlchemy
       * Chameleon
       * security
   * - `blogr`_ (英語)
     - 4h
     - ``pyramid_blogr`` チュートリアル
     - Flask ウェブフレームワークチュートリアルの Flaskr アプリにヒントを得た
     - `pyramid_blogr`_
     - * URL dispatch
       * SQLAlchemy
       * Mako
       * security
       * WTForms
       * pagination
   * - `birdie`_ (英語)
     - 4h
     - Birdie チュートリアル: シンプルな Twitter クローン
     - OSCON 2011 と PyCon USA 2012 で Carlos de la Guardia によって発表された
     - `cguardia_tut`_
     -


.. .. _firstapp: http://docs.pylonsproject.org/projects/pyramid/en/1.4-branch/narr/firstapp.html
.. .. _wiki: http://docs.pylonsproject.org/projects/pyramid/en/1.4-branch/tutorials/wiki/index.html
.. .. _wiki2: http://docs.pylonsproject.org/projects/pyramid/en/1.4-branch/tutorials/wiki2/index.html
.. .. _single_file: http://docs.pylonsproject.org/projects/pyramid_tutorials/en/latest/single_file_tasks/single_file_tasks.html
.. .. _humans: http://docs.pylonsproject.org/projects/pyramid_tutorials/en/latest/humans/index.html
.. .. _getting_started: http://docs.pylonsproject.org/projects/pyramid_tutorials/en/latest/getting_started/index.html
.. .. _blogr: http://pyramid-blogr.readthedocs.org/en/latest/
.. .. _birdie: https://github.com/cguardia/Pyramid-Tutorial/blob/master/presentation/pyramid_tutorial.pdf

.. .. _Narrative Documentation: http://docs.pylonsproject.org/projects/pyramid/en/1.4-branch/#narrative-documentation
.. .. _Tutorials: http://docs.pylonsproject.org/projects/pyramid/en/1.4-branch/#tutorials

.. .. _pyramid: https://github.com/Pylons/pyramid
.. .. _pyramid_tutorials: https://github.com/Pylons/pyramid_tutorials
.. .. _pyramid_blogr: https://github.com/Pylons/pyramid_blogr
.. .. _cguardia_tut: https://github.com/cguardia/Pyramid-Tutorial


.. _firstapp: http://docs.pylonsproject.jp/projects/pyramid-doc-ja/en/1.4-branch-doc-ja/narr/firstapp.html
.. _wiki: http://docs.pylonsproject.jp/projects/pyramid-doc-ja/en/1.4-branch-doc-ja/tutorials/wiki/index.html
.. _wiki2: http://docs.pylonsproject.jp/projects/pyramid-doc-ja/en/1.4-branch-doc-ja/tutorials/wiki2/index.html
.. _single_file: http://docs.pylonsproject.jp/projects/pyramid_tutorials-doc-ja/en/latest/single_file_tasks/single_file_tasks.html
.. _humans: http://docs.pylonsproject.jp/projects/pyramid_tutorials-doc-ja/en/latest/humans/index.html
.. _getting_started: http://docs.pylonsproject.jp/projects/pyramid_tutorials-doc-ja/en/latest/getting_started/index.html
.. _blogr: http://pyramid-blogr.readthedocs.org/en/latest/
.. _birdie: https://github.com/cguardia/Pyramid-Tutorial/blob/master/presentation/pyramid_tutorial.pdf

.. _Narrative Documentation: http://docs.pylonsproject.jp/projects/pyramid-doc-ja/en/1.4-branch-doc-ja/#id2
.. _Tutorials: http://docs.pylonsproject.jp/projects/pyramid-doc-ja/en/1.4-branch-doc-ja/#id3

.. _pyramid: https://github.com/Pylons/pyramid
.. _pyramid_tutorials: https://github.com/Pylons/pyramid_tutorials
.. _pyramid_blogr: https://github.com/Pylons/pyramid_blogr
.. _cguardia_tut: https://github.com/cguardia/Pyramid-Tutorial


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
