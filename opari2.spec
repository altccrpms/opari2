Name:           opari2
Version:        2.0
Release:        1%{?dist}
Summary:        An OpenMP runtime performance measurement instrumenter

License:        BSD
URL:            http://www.vi-hps.org/projects/score-p/
Source0:        http://www.vi-hps.org/upload/packages/%{name}/%{name}-%{version}.tar.gz

BuildRequires:   gcc-gfortran

%description
OPARI2 is a source-to-source instrumentation tool for OpenMP and hybrid
codes.  It surrounds OpenMP directives and runtime library calls with calls
to the POMP2 measurement interface.

OPARI2 will provide you with a new initialization method that allows for
multi-directory and parallel builds as well as the usage of pre-instrumented
libraries. Furthermore, an efficient way of tracking parent-child
relationships was added. Additionally, we extended OPARI2 to support
instrumentation of OpenMP 3.0 tied tasks.


%prep
%setup -q


%build
%configure --disable-static --disable-silent-rules --with-platform=linux
make %{?_smp_mflags}


%install
%make_install
find %{buildroot} -name '*.la' -delete -print
find %{buildroot}%{_defaultdocdir}/%{name}/example* -name '*.a' -delete -print
# Avoid duplicated filelist with %%doc
cp -p AUTHORS ChangeLog README %{buildroot}%{_defaultdocdir}/%{name}/


%check
make check


%files
%license COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}-config
%{_libexecdir}/pomp2-parse-init-regions.awk
%{_includedir}/%{name}/
%{_defaultdocdir}/%{name}/
%{_datadir}/%{name}/


%changelog
* Fri Apr 15 2016 Orion Poplawski <orion@cora.nwra.com> - 2.0-1
- Update to 2.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Orion Poplawski <orion@cora.nwra.com> - 1.1.4-7
- Update to 1.1.4

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 8 2015 Orion Poplawski <orion@cora.nwra.com> - 1.1.3-1
- Update to 1.1.3

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1.2-6
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 28 2014 Orion Poplawski <orion@cora.nwra.com> - 1.1.2-3
- Add %%check
- Disable silent build

* Wed Feb 26 2014 Orion Poplawski <orion@cora.nwra.com> - 1.1.2-2
- Spec cleanup

* Wed Feb 26 2014 Orion Poplawski <orion@cora.nwra.com> - 1.1.2-1
- Update to 1.1.2

* Sun Oct 6 2013 Orion Poplawski <orion@cora.nwra.com> - 1.1.1-2
- Drop -devel sub-package
- New summary

* Wed Sep 25 2013 Orion Poplawski <orion@cora.nwra.com> - 1.1.1-1
- Update to 1.1.1

* Mon Apr 15 2013 Orion Poplawski <orion@cora.nwra.com> - 1.0.7-2
- Add patch to put awk script into libexecdir

* Wed Apr 3 2013 Orion Poplawski <orion@cora.nwra.com> - 1.0.7-1
- Initial package
