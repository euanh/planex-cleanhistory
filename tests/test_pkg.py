# Run these tests with 'nosetests':
#   install the 'python-nose' package (Fedora/CentOS or Ubuntu)
#   run 'nosetests' in the root of the repository

import unittest

import pkg

class BasicTests(unittest.TestCase):
    def setUp(self):
        self.spec = pkg.Spec("SPECS/ocaml-cohttp.spec")

    def test_name(self):
        assert self.spec.name() == "ocaml-cohttp"

    def test_version(self):
        assert self.spec.version() == "0.9.8"

    def test_provides(self):
        assert self.spec.provides() == \
            set(["ocaml-cohttp", "ocaml-cohttp(x86-64)",
                 "ocaml-cohttp-devel", "ocaml-cohttp-devel(x86-64)"])

    def test_sources(self):
        assert sorted(self.spec.sources()) == \
            sorted(["https://github.com/mirage/ocaml-cohttp/archive/ocaml-cohttp-0.9.8/ocaml-cohttp-0.9.8.tar.gz"])

    def test_buildrequires(self):
        assert self.spec.buildrequires() == \
            set(["ocaml", "ocaml-findlib", "ocaml-re-devel",
                 "ocaml-uri-devel", "ocaml-cstruct-devel",
                 "ocaml-lwt-devel", "ocaml-ounit-devel",
                 "ocaml-ocamldoc", "ocaml-camlp4-devel",
                 "openssl", "openssl-devel"])

    def test_source_package_name(self):
        assert self.spec.source_package_name() == \
            "ocaml-cohttp-0.9.8-1.el6.src.rpm"

    def test_binary_package_names(self):
        assert sorted(self.spec.binary_package_names()) == \
            sorted(["x86_64/ocaml-cohttp-0.9.8-1.el6.x86_64.rpm",
             "x86_64/ocaml-cohttp-devel-0.9.8-1.el6.x86_64.rpm"])

