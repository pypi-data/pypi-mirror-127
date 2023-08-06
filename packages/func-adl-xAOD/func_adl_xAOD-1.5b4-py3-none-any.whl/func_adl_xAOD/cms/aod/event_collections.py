import func_adl_xAOD.common.cpp_types as ctyp
from func_adl_xAOD.common.event_collections import (
    EventCollectionSpecification, event_collection_coder, event_collection_collection, event_collection_container)


# class cms_aod_event_collection_container(event_collection_container):
#     'There is nothing turned on here - till we have a real use case.'
#     def __init__(self, type_name, is_pointer=True):
#         super().__init__(type_name, is_pointer)

#     def __str__(self):
#         return f"edm::Handle<{self._type_name}>"


class cms_aod_event_collection_collection(event_collection_collection):
    def __init__(self, type_name, element_name, is_type_pointer=True, is_element_pointer=True):
        super().__init__(type_name, element_name, is_type_pointer, is_element_pointer)

    def __str__(self):
        return f"edm::Handle<{self._type_name}>"


# all the collections types that are available. This is required because C++
# is strongly typed, and thus we have to transmit this information.
cms_aod_collections = [
    EventCollectionSpecification('cms', "Tracks",
                                 ['DataFormats/TrackReco/interface/Track.h',
                                  'DataFormats/TrackReco/interface/TrackFwd.h',
                                  'DataFormats/TrackReco/interface/HitPattern.h'
                                  ],
                                 cms_aod_event_collection_collection('reco::TrackCollection', 'reco::Track'),
                                 [],
                                 ),
    EventCollectionSpecification('cms', "TrackMuons",
                                 ['DataFormats/MuonReco/interface/Muon.h',
                                  'DataFormats/MuonReco/interface/MuonFwd.h',
                                  'DataFormats/MuonReco/interface/MuonSelectors.h',
                                  'DataFormats/MuonReco/interface/MuonIsolation.h',
                                  'DataFormats/MuonReco/interface/MuonPFIsolation.h',
                                  'DataFormats/TrackReco/interface/Track.h',
                                  'DataFormats/TrackReco/interface/TrackFwd.h',
                                  'DataFormats/TrackReco/interface/HitPattern.h'
                                  ],
                                 cms_aod_event_collection_collection('reco::TrackCollection', 'reco::Track'),
                                 [],
                                 ),
    EventCollectionSpecification('cms', "Muons",
                                 ['DataFormats/MuonReco/interface/Muon.h',
                                  'DataFormats/MuonReco/interface/MuonFwd.h',
                                  'DataFormats/MuonReco/interface/MuonSelectors.h',
                                  'DataFormats/MuonReco/interface/MuonIsolation.h',
                                  'DataFormats/MuonReco/interface/MuonPFIsolation.h'
                                  ],
                                 cms_aod_event_collection_collection('reco::MuonCollection', 'reco::Muon'),
                                 [],
                                 ),
    EventCollectionSpecification('cms', "Vertex",
                                 ["DataFormats/VertexReco/interface/Vertex.h",
                                  "DataFormats/VertexReco/interface/VertexFwd.h"
                                  ],
                                 cms_aod_event_collection_collection('reco::VertexCollection', 'reco::Vertex', is_element_pointer=False),
                                 [],
                                 ),
    EventCollectionSpecification('cms', "GsfElectrons",
                                 ['DataFormats/EgammaCandidates/interface/GsfElectron.h',
                                  'DataFormats/GsfTrackReco/interface/GsfTrack.h',
                                  'DataFormats/GsfTrackReco/interface/GsfTrackFwd.h'
                                  ],
                                 cms_aod_event_collection_collection('reco::GsfElectronCollection', 'reco::GsfElectron'),
                                 [],
                                 ),
]


def define_default_cms_types():
    'Define the default cms types'
    ctyp.add_method_type_info("reco::Track", "hitPattern", ctyp.terminal('reco::HitPattern'))

    ctyp.add_method_type_info("reco::Muon", "globalTrack", ctyp.terminal('reco::Track', is_pointer=True))
    ctyp.add_method_type_info("reco::Muon", "hitPattern", ctyp.terminal('reco::HitPattern'))
    ctyp.add_method_type_info("reco::Muon", "isPFIsolationValid", ctyp.terminal('bool'))
    ctyp.add_method_type_info("reco::Muon", "isPFMuon", ctyp.terminal('bool'))
    ctyp.add_method_type_info("reco::Muon", "pfIsolationR04", ctyp.terminal('reco::MuonPFIsolation'))

    ctyp.add_method_type_info("reco::GsfElectron", "gsfTrack", ctyp.terminal('reco::GsfTrack', is_pointer=True))
    ctyp.add_method_type_info("reco::GsfElectron", "isEB", ctyp.terminal('bool'))
    ctyp.add_method_type_info("reco::GsfElectron", "isEE", ctyp.terminal('bool'))
    ctyp.add_method_type_info("reco::GsfElectron", "passingPflowPreselection", ctyp.terminal('bool'))
    ctyp.add_method_type_info("reco::GsfElectron", "superCluster", ctyp.terminal('reco::SuperClusterRef', is_pointer=True))
    ctyp.add_method_type_info("reco::GsfElectron", "pfIsolationVariables", ctyp.terminal('reco::GsfElectron::PflowIsolationVariables'))

    ctyp.add_method_type_info("reco::GsfTrack", "trackerExpectedHitsInner", ctyp.terminal('reco::HitPattern'))  # reco::HitPattern is the expected return type


class cms_event_collection_coder(event_collection_coder):
    def get_running_code(self, container_type: event_collection_container) -> list:
        return [f'{container_type} result;',
                'iEvent.getByLabel(collection_name, result);']
