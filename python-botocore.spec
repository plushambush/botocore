%global pkgname botocore
%define buildid @BUILDID@

Name:           python-%{pkgname}
# NOTICE - Updating this package requires updating python-boto3
Version:        1.20.14
Release:        CROC12%{?buildid}%{?dist}
Summary:        Low-level, data-driven core of boto 3

License:        ASL 2.0
URL:            https://github.com/C2Devel/botocore.git
Source0:        https://pypi.io/packages/source/b/botocore/botocore-%{version}.tar.gz
BuildArch:      noarch

%description
A low-level interface to a growing number of Amazon Web Services. The
botocore package is the foundation for the AWS CLI as well as boto3.

%package -n     python2-%{pkgname}
Summary:        Low-level, data-driven core of boto 3
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
Provides:       python2-%{pkgname}
Requires:       python2-jmespath >= 0.7.1
Requires:       python2-dateutil >= 2.1
Requires:       python2-urllib3 >= 1.24.1

%description -n python2-%{pkgname}
A low-level interface to a growing number of Amazon Web Services. The
botocore package is the foundation for the AWS CLI as well as boto3.

%package -n     python%{python3_pkgversion}-%{pkgname}
Summary:        Low-level, data-driven core of boto 3
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
Provides:       python%{python3_pkgversion}-%{pkgname}
Requires:       python%{python3_pkgversion}-jmespath >= 0.7.1
Requires:       python%{python3_pkgversion}-dateutil >= 2.1
Requires:       python%{python3_pkgversion}-urllib3 >= 1.24.1

%description -n python%{python3_pkgversion}-%{pkgname}
A low-level interface to a growing number of Amazon Web Services. The
botocore package is the foundation for the AWS CLI as well as boto3.

%prep
%setup -q -n %{pkgname}-%{version}
rm -rf %{pkgname}.egg-info
# Remove online tests
rm -rf tests/integration

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%files -n python2-%{pkgname}
%doc README.rst
%license LICENSE.txt
%{python2_sitelib}/%{pkgname}/
%{python2_sitelib}/%{pkgname}-*.egg-info/

%files -n python%{python3_pkgversion}-%{pkgname}
%doc README.rst
%license LICENSE.txt
%{python3_sitelib}/%{pkgname}/
%{python3_sitelib}/%{pkgname}-*.egg-info/

%changelog
* Tue Mar 01 2022 Ivan Konov <ikonov@croc.ru> - 1.20.14-CROC11
- ec2: add Description to ModifySnapshotAttributeRequest

* Mon Feb 07 2022 Alexander Chernev <achernev@croc.ru> - 1.20.14-CROC10
- Technical Release

* Mon Feb 07 2022 Alexander Chernev <achernev@croc.ru> - 1.20.14-CROC9
- botocore: data: ec2: add CreateVolumeExportTask method
- botocore: data: ec2: add DescribeExportVolumeTasks method
- botocore: data: ec2: add Notify and Email fields to IE requests
- botocore: data: ec2: add Progress field to ExportTask structure
- eks: change requestUri of ModifyWorkersInstanceType method
- botocore: data: ec2: add VirtualizationType to ImportImage request
- botocore: data: ec2: add ImageName, Notify, Email to ImportImage request
- ec2: add volume versions

* Mon Nov 29 2021 Konstantin Zakharov <kzakharov@croc.ru> - 1.20.14-CROC8
- spec: revert build for py2
- eks: add ModifyWorkersInstanceType operations

* Wed Nov 24 2021 Evgeny Kovalev <evgkovalev@croc.ru> - 1.20.14-CROC7
- eks: add ModifyUserData operations

* Tue Oct 26 2021 Alex Rudenko <arudenko@croc.ru> - 1.20.14-CROC6
- spec: add urllib3 1.25.6 to dependencies
- spec: remove build for py2

* Wed Oct 20 2021 Andrey Kulaev <akulaev@croc.ru> - 1.20.14-CROC5
- eks: use an already allocated public ip address
- eks: show EbsUser field
- eks: add Pod and Service Subnet CIDR to cluster model

* Mon Aug 23 2021 Andrey Kulaev <akulaev@croc.ru> - 1.20.14-CROC4
- eks: deploying a high availability cluster in multiple AZ
- eks: add ModifySecurityGroups operations
- eks: add shapes Instance and InstanceList
- eks: use SecurityGroupIds instead of SecurityGroups

* Fri Jul 02 2021 Andrey Kulaev <akulaev@croc.ru> - 1.20.14-CROC3
- eks: fix shape name typo Bool -> Boolean

* Mon Jun 28 2021 Max Kotov <makotov@croc.ru> - 1.20.14-CROC2
- Introduce KS Public API

* Wed Feb 24 2021 Alexander Chernev <achernev@croc.ru> - 1.20.14-CROC1
- Update to latest botocore - 1.20.14
