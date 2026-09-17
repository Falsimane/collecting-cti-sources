# Attacks Against Customer Service Centers by Impersonation of Potential Clients

- **Source :** ClearSky Cybersecurity
- **URL :** https://www.clearskysec.com/customer-service-centers-attacks/
- **Date :** 2016-11-19

---

Hundreds of customer service centers have been targeted In a campaign going back at least to August 2016.

An email is sent to the “contact us” or “customer support” address of an online shop. The sender pretends to be a a customer that has a problem with the online shopping cart or is just asking to make sure products are available in stock.

The sender attaches a Word document to the email, and says that it lists the items he or she would like to purchase, or otherwise tries to entice the recipient to open the document.

For example:

_Hello Customer Support,_

_I would like to place an order on <name of organisation>, however not certain if a couple items are in Stock. I have listed in the enclosed doc all I am interested in purchasing, can you review it and confirm if you have it in stock?_

_Thank you for your assistance._

_Best Regards!_

The Word documents contains Macro code that would infect the computer if enabled by the recipient.

In the samples we analysed, the malicious document communicated to the following address:

http://**excelcenter[.]ro** /port10/owalogon.asp

## Samples

Below are 30 samples from the campaign, hundreds more exist. Note that the name of the malicious documents usually includes the domain name of the targeted company with a .doc suffix.

Ocovildovinil.Pt.doc  
df8dfdad1eef284ea90c30a903a4692bd6cc4fca0e3a5b682b07bf7de977cdfb

Oponeo.Pl.doc  
de2d892c281cba898cec22cd93ca26a22cb631f910c5c88d7bd4336b3cd8b1ee

Edelweissfin.Com.doc  
d274f0568f19066aa374339033607a07d8c2f243437edbbcfd4e30605a8ffe28

Eslite.Com.doc  
7bfffdb966111459a745a10a9f515025af299ea5f69ab727619b2551dbda9aa2

Outdoorsportstravel.Asia.doc  
865dbf107da63ff91fb3af3331b759f774203c20ddc833e8741227ca16ae2e48

Luxapool.Com.Au.doc  
cf8b8704a4cf106fff62d16d8b1986523b8d1e54cbed8dc10c766d9ec8799d8f

Biminitop.De.doc  
c4722b56730643f41b1829effbd31173a1fd84a0465d7bd54ee322c4c4b373f9

Blaudruckstoffe.De.doc  
4e0838501907cdc08c6dbc2f4ac2d77f4567bb59743f205259c777988b3bb41b

Innout.Com.doc  
6e64874bf64194d06201063c5afbc838019c804e6c22b3d30366e6f65e81a16e

Triodepot.Com.doc  
60a53af4e63a1205ccd766223c8bf4d77cebb252b3c8585113fbf8b7002c0717

Tailoredliving.Com.doc  
cf7746f4700e06091a92abf8a04bcf24108aa5159fffbb5125caaa2bea0440ad

Tsrhockey.Com.doc  
f9680d3ca4a9579c065fedbc51d5b4edf229568fc88062c7f35b5d07c3ed87ee

Priberam.Pt.doc  
5fbb01dae7d1a7791830b389ce9477fadc9796e1a254a22b639cdcb481031b9f

Pctvsystems.Com.doc  
56c5c92907e5b8cfa807356f11eb9cc6bc64fe4a49b1eb88ac7f30a339e5d6be

Sickkidsfoundation.Com.doc  
a712db7e2b022ee49c26fd1f188e9c9df7dd810c3e1f279e53435284acb44215

Agawa.Pl.doc  
450c4793d0b8ba6d3a7294812e371971de481e3a0ed174cd3a7e3bdfafaa6ee4

Sm-Moto.Com.doc  
ad30c40320561b2fe01420c287add294c4cdc459ee9a24fb4ccaa5a8f472267c

Guggenheiminvestments.Com.doc  
0f1770106a960329f978986209e5918e0e6539f80bcf2f3719d23ce39c5cc1b9

Voedingscentrum.Nl.doc  
9fe0bd7031f42252c6dc0b9ac41f33e252d7a067a8eb68ec51cf3c5cbb2acdcc

Danskebank.Fi.doc  
c816ff922125cf17db3780a6f0027b106d713e7fde4f63efd7f9d11f78b4114f

Thisisaka.Com.doc  
54e83553714a5fa6fc249f870c0200e5a679cd5ec2f17b3d3168bbcdf7eec869

Bristolwest.Com.doc  
67657c4bdb9968f14ceed73942bf71c341ae9264bd474884b363e840b5d60470

Dokomo.Be.doc  
eab3b8a4240bdebde634312d08737586fd1111651fc4980a1254439d436086fe

Rikstoto.No.doc  
59d4307d35f35cbca00131c43bb28b48acac3035f7b7ecfcc9b91009de8f7ef0

Maisondelin.Fr.doc  
525e40bd5997bfc48e4b76add60b21faff238d1913bf6964bdcbc3c753b71026

Moposport.Fi.doc  
8fac72b5c5063411645c7d7d5201b55aaf37fa3201029f783b7be1ab178732d1

Lichtkoepeltje.Nl.doc  
9938208842966e9b7505cffec36ef19b0668843bb534d65a7568e484a7a29b28

Gartenmoebel24.De.docx  
1770de62c68d4d2325926dce555b70477a6baa02faf87384f69c5adc5ac7e514

Komino.Pl.doc  
4f2110e091a5f86e8952748e788bc0cb38905c60d91e01edcdce43047db119e6

Skins.Net.doc  
839347259d1f063e3f2b9bc09c5257ff287c1064349350a8407eb5a9188eb092

## Acknowledgments

We would like to thank Matan Scharf of [Cycuro](https://cycuro.com/) for his assistant in the investigation.