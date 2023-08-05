#pragma once

#include "esphome/components/modbus_controller/modbus_controller.h"
#include "esphome/components/switch/switch.h"
#include "esphome/core/component.h"

namespace esphome {
namespace modbus_controller {

class ModbusSwitch : public Component, public switch_::Switch, public SensorItem {
 public:
  ModbusSwitch(ModbusRegisterType register_type, uint16_t start_address, uint8_t offset, uint32_t bitmask,
               bool force_new_range)
      : Component(), switch_::Switch() {
    this->register_type = register_type;
    this->start_address = start_address;
    this->offset = offset;
    this->bitmask = bitmask;
    this->sensor_value_type = SensorValueType::BIT;
    this->skip_updates = 0;
    this->register_count = 1;
    if (register_type == ModbusRegisterType::HOLDING || register_type == ModbusRegisterType::COIL) {
      this->start_address += offset;
      this->offset = 0;
    }
    this->force_new_range = force_new_range;
  };
  void setup() override;
  void write_state(bool state) override;
  void dump_config() override;
  void set_state(bool state) { this->state = state; }
  void parse_and_publish(const std::vector<uint8_t> &data) override;
  void set_parent(ModbusController *parent) { this->parent_ = parent; }

  using transform_func_t = std::function<optional<bool>(ModbusSwitch *, bool, const std::vector<uint8_t> &)>;
  void set_template(transform_func_t &&f) { this->publish_transform_func_ = f; }

 protected:
  ModbusController *parent_;
  optional<transform_func_t> publish_transform_func_{nullopt};
};

}  // namespace modbus_controller
}  // namespace esphome
