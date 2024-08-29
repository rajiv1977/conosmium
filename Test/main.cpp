#include <iostream>

#include <osmium/handler.hpp>
#include <osmium/io/any_input.hpp>
#include <osmium/osm/node.hpp>
#include <osmium/osm/way.hpp>
#include <osmium/visitor.hpp>

class MyHandler : public osmium::handler::Handler {
public:
    void way(const osmium::Way& way) {
        std::cout << "way " << way.id() << '\n';
        for (const osmium::Tag& t : way.tags()) {
            std::cout << t.key() << "=" << t.value() << '\n';
        }
    }

    void node(const osmium::Node& node) {
        std::cout << "node " << node.id() << '\n';
    }
};

int main() {
    auto otypes = osmium::osm_entity_bits::node | osmium::osm_entity_bits::way;
    osmium::io::Reader reader{"sample1.osm", otypes}; // get the input file from data folder
    MyHandler handler;
    osmium::apply(reader, handler);
    reader.close();
}


