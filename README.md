# torrc
simple Python script to influence the locations of selected tor servers

This small Python script creates a torrc file that ensures that the Tor browser only selects GuardNodes, MiddleNodes and ExitNodes from certain countries according to the desired pattern. To keep things simple, only country abbreviations are used in which significant Tor servers can be found. This means that two tor servers in one routing are never in the same country and investigations are made more difficult by using more GuardNodes and dividing the servers in use into rough political camps. After the download, you simply have to save the output of the script in the file:

~/Downloads/tor-browser-linux-x86_64-14.0.6/tor-browser/Browser/TorBrowser/Data/Tor/torrc

This could then look like the following, for example:

StrictNodes 1
NumEntryGuards 10
EntryNodes {ru},{ua},{al},{in},{sg},{am},{tr},{ba},{rs},{jp},{br},{my},{za},{bd},{kr}
MiddleNodes {us},{gb},{ch},{ca},{au},{il}
ExitNodes {nl},{fr},{se},{pl},{fi},{at},{cz},{lu},{ro},{it},{dk},{es},{bg},{hu},{ie},{lt},{pt}
ExcludeNodes {de}
