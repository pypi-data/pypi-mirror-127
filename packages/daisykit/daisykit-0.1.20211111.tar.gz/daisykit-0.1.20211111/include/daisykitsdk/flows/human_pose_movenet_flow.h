// Copyright 2021 The DaisyKit Authors.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#ifndef DAISYKIT_FLOWS_PUSHUP_COUNTER_FLOW_H_
#define DAISYKIT_FLOWS_PUSHUP_COUNTER_FLOW_H_

#include "daisykitsdk/models/body_detector.h"
#include "daisykitsdk/models/pose_detector_movenet.h"

#include <atomic>
#include <mutex>
#include <opencv2/opencv.hpp>
#include <string>

namespace daisykit {
namespace flows {
class HumanPoseMoveNetFlow {
 public:
  HumanPoseMoveNetFlow(const std::string& config_str);

  void Process(cv::Mat& rgb);
  void DrawResult(cv::Mat& rgb);

 private:
  std::vector<types::Object> bodies_;
  std::mutex bodies_lock_;

  std::vector<std::vector<types::Keypoint>> keypoints_;
  std::mutex keypoints_lock_;

  models::BodyDetector* body_detector_;
  models::PoseDetectorMoveNet* pose_detector_;
};

}  // namespace flows
}  // namespace daisykit

#endif
