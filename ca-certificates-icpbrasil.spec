Name:           ca-certificates-icpbrasil
Version:        2020.01.09
Release:        1
Summary:        Certificados das ACs da ICP-Brasil
License:        GPL-2.0+
Group:          Productivity/Networking/Security
Url:            https://www.iti.gov.br/repositorio/repositorio-ac-raiz
Source0:        ACcompactado.zip
Source1:        hashsha512.txt
# Arquivos baixados em: https://www.iti.gov.br/repositorio/84-repositorio/489-certificados-das-acs-da-icp-brasil-arquivo-unico-compactado
# Atualizados em: 09 de janeiro de 2020
Source2:        instalar-icpbrasil
Source3:        icpbrasil.sh

BuildArch:      noarch
BuildRequires:  unzip

Requires:       mozilla-nss-tools
Requires:       openssl

Requires(post):     ca-certificates
Requires(postun):   ca-certificates


%description
Este pacote contém todos os certificados das ACs da ICP-Brasil.

Para instalar os certificados no seu perfil de usuário, execute o comando:

$ instalar-icpbrasil

Esse script suporta:

- o navegador Mozilla Firefox
- os navegadores Google Chrome/Chromium
- quaisquer navegadores baseados nos supracitados (Opera, Vivaldi, Brave, etc)
- o cliente de e-mail Mozilla Thunderbird

Para navegadores instalados após este pacote, pode ser necessário executar esse
comando novamente.

Para novos usuários criados após a instalação deste pacote, os certificados são
instalados automaticamente nos navegadores Google Chrome/Chromium e derivados.

Esse script deve ser executado para cada usuário no computador (não há como
instalar os certificados em todos os navegadores a nível de sistema).


%prep
cd %{_sourcedir}
sha512sum -c %{SOURCE1}
%setup -c


%build


%install
mkdir -p %{buildroot}%{_datadir}/icpbrasil/
install -D -m 644 *.crt %{buildroot}%{_datadir}/icpbrasil/

mkdir -p %{buildroot}%{_datadir}/pki/trust/anchors/
for certificado in *.crt
do
    ln -s "%{_datadir}/icpbrasil/$certificado" "%{buildroot}%{_datadir}/pki/trust/anchors/$certificado"
done

mkdir -p %{buildroot}%{_bindir}/
install -D -m 555 %{SOURCE2} %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_sysconfdir}/profile.d/
install -D -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/profile.d/


%post
update-ca-certificates || true


%postun
update-ca-certificates || true


%files
%defattr(-,root,root)
%config %{_sysconfdir}/profile.d/icpbrasil.sh
%{_bindir}/instalar-icpbrasil
%{_datadir}/icpbrasil/
%{_datadir}/pki/trust/anchors/*.crt


%changelog

