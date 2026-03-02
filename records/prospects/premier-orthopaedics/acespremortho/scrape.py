#!/usr/bin/env python3
"""Scrape all acespremortho.com pages via Jina Reader API and save as .md files."""

import os
import time
from typing import Optional
import requests
from urllib.parse import urlparse
from pathlib import Path

JINA_API_KEY = os.environ.get("JINA_API_KEY", "jina_85c13e7577184a31b90d92ee1f94bb3f78XIYUV8kTnWQO0QrMWy-4QzCv6w")
OUTPUT_DIR = Path(__file__).parent
JINA_BASE = "https://r.jina.ai/"

URLS = [
    # --- Pages (30) ---
    "https://acespremortho.com/",
    "https://acespremortho.com/meet-the-providers/",
    "https://acespremortho.com/dr-jillian-karpyshyn/",
    "https://acespremortho.com/dr-ravinder-tikoo/",
    "https://acespremortho.com/robotic-surgery/",
    "https://acespremortho.com/our-promise-to-our-patients/",
    "https://acespremortho.com/blog/",
    "https://acespremortho.com/before-and-after-surgery/",
    "https://acespremortho.com/contact-us/",
    "https://acespremortho.com/insurance-coverage-2/",
    "https://acespremortho.com/insurance-coverage/",
    "https://acespremortho.com/dr-howard-baruch/",
    "https://acespremortho.com/dr-debra-pertrucci/",
    "https://acespremortho.com/dr-aditya-patel/",
    "https://acespremortho.com/dr-iris-drey/",
    "https://acespremortho.com/dr-barry-finkelstein/",
    "https://acespremortho.com/jay-s-reidler-md-mph/",
    "https://acespremortho.com/terms-conditions/",
    "https://acespremortho.com/terms-conditions-2/",
    "https://acespremortho.com/patient-education/",
    "https://acespremortho.com/motor-vehicle-accidents/",
    "https://acespremortho.com/independent-medical-examinations/",
    "https://acespremortho.com/medical-records-document-services/",
    "https://acespremortho.com/workers-compensation-injuries/",
    "https://acespremortho.com/testimonials/",
    "https://acespremortho.com/patient-forms/",
    "https://acespremortho.com/spine-care-faq/",
    "https://acespremortho.com/associated-organizations/",
    "https://acespremortho.com/specialties/",
    "https://acespremortho.com/treatments/",
    # --- Posts (63) ---
    "https://acespremortho.com/blog/the-role-of-robotics-in-joint-replacement-surgery-precision-speed-and-recovery-benefits/",
    "https://acespremortho.com/blog/shoulder-and-hand-surgery-when-conservative-treatments-are-no-longer-enough/",
    "https://acespremortho.com/specialties/hand-shoulder/",
    "https://acespremortho.com/blog/how-regenerative-medicine-enhances-pain-management-and-speeds-up-recovery/",
    "https://acespremortho.com/blog/managing-acute-injuries-pain-relief-strategies-for-sprains-fractures-and-muscle-tears/",
    "https://acespremortho.com/blog/non-surgical-solutions-for-chronic-pain-how-we-help-improve-your-quality-of-life/",
    "https://acespremortho.com/blog/the-importance-of-pain-management-in-hip-and-knee-replacement-recovery/",
    "https://acespremortho.com/spinal-conditions/neck-pain/",
    "https://acespremortho.com/uncategorized/pain-management-service/",
    "https://acespremortho.com/services/spine-surgery/",
    "https://acespremortho.com/services/orthopaedics-hand-shoulder-surgery/",
    "https://acespremortho.com/specialties/foot-ankle/",
    "https://acespremortho.com/specialties/pain-management-specialists/",
    "https://acespremortho.com/specialties/sports-medicine-specialists/",
    "https://acespremortho.com/services/foot-ankle-procedures/",
    "https://acespremortho.com/services/pain-management-treatments/",
    "https://acespremortho.com/blog/pain-management-after-surgery-how-effective-pain-control-enhances-recovery/",
    "https://acespremortho.com/blog/advanced-imaging-and-treatments-for-shoulder-injuries/",
    "https://acespremortho.com/blog/minimally-invasive-options-for-rotator-cuff-tears/",
    "https://acespremortho.com/blog/comprehensive-shoulder-and-hand-surgery-after-trauma/",
    "https://acespremortho.com/blog/hip-osteoarthritis-non-surgical-treatments-to-alleviate-pain-and-improve-function/",
    "https://acespremortho.com/blog/when-to-consider-hip-replacement-surgery-for-osteoarthritis-pain-relief/",
    "https://acespremortho.com/blog/knee-ligament-injuries-acl-mcl-pcl-lcl-surgical-and-non-surgical-treatment-options/",
    "https://acespremortho.com/blog/hip-bursitis-how-targeted-therapies-can-relieve-pain-and-improve-mobility/",
    "https://acespremortho.com/blog/understanding-herniated-discs-symptoms-diagnosis-and-treatment-options/",
    "https://acespremortho.com/blog/degenerative-disc-disease-non-surgical-solutions-for-long-term-pain-relief/",
    "https://acespremortho.com/blog/spinal-deformities-how-surgery-can-correct-scoliosis-kyphosis-and-lordosis/",
    "https://acespremortho.com/blog/bunions-surgical-treatment-options-for-pain-and-deformity-relief/",
    "https://acespremortho.com/uncategorized/sports-medicine/",
    "https://acespremortho.com/blog/introduction-to-orthopedics-understanding-the-musculoskeletal-system/",
    "https://acespremortho.com/blog/common-orthopedic-conditions/",
    "https://acespremortho.com/blog/orthopedic-diagnostics-x-rays-mri-and-ct-scans/",
    "https://acespremortho.com/blog/non-surgical-orthopedic-treatments-physical-therapy-and-rehabilitation/",
    "https://acespremortho.com/blog/types-of-orthopedic-surgeries-explained/",
    "https://acespremortho.com/blog/joint-replacement-surgery-what-to-expect/",
    "https://acespremortho.com/blog/arthroscopic-surgery-key-insights/",
    "https://acespremortho.com/blog/orthopedic-trauma-surgery-managing-accidents-and-injuries/",
    "https://acespremortho.com/blog/understanding-concussions-safe-management-and-recovery-for-athletes/",
    "https://acespremortho.com/blog/overuse-injuries-in-sports-prevention-treatment-and-how-to-avoid-recurrence/",
    "https://acespremortho.com/blog/tendonitis-in-athletes-minimizing-pain-and-enhancing-recovery-with-targeted-treatment/",
    "https://acespremortho.com/blog/cartilage-injuries-innovative-treatments-for-repetitive-stress-or-trauma-to-joints/",
    "https://acespremortho.com/blog/when-surgery-is-the-best-solution-for-chronic-shoulder-pain/",
    "https://acespremortho.com/blog/spinal-stenosis-how-we-use-advanced-technology-to-alleviate-pain-and-restore-mobility/",
    "https://acespremortho.com/blog/foot-ankle-fractures-when-surgery-is-necessary-for-proper-healing/",
    "https://acespremortho.com/blog/achilles-tendon-injuries-non-surgical-and-surgical-approaches-to-treatment/",
    "https://acespremortho.com/blog/plantar-fasciitis-how-our-specialists-provide-relief-with-personalized-treatment-plans/",
    "https://acespremortho.com/blog/foot-ankle-arthritis-joint-replacement-and-fusion-for-pain-free-movement/",
    "https://acespremortho.com/blog/chronic-pain-management-addressing-long-term-conditions-with-targeted-therapies/",
    "https://acespremortho.com/blog/the-role-of-pain-management-in-spinal-injuries-and-disorders/",
    "https://acespremortho.com/specialties/hip-knee/",
    "https://acespremortho.com/services/orthopaedics-hip-knee-surgery/",
    "https://acespremortho.com/specialties/neck-back/",
    "https://acespremortho.com/uncategorized/how-long-do-artificial-joints-last/",
    "https://acespremortho.com/blog/what-is-an-orthopaedic-surgeon/",
    "https://acespremortho.com/blog/what-is-arthroscopic-surgery/",
    "https://acespremortho.com/blog/what-is-joint-replacement-surgery/",
    "https://acespremortho.com/blog/what-is-physical-medicine-and-rehabilitation/",
    "https://acespremortho.com/blog/what-is-a-physiatrist/",
    "https://acespremortho.com/blog/what-is-acl-reconstruction/",
    "https://acespremortho.com/blog/what-happens-during-rotator-cuff-surgery/",
    "https://acespremortho.com/blog/breaking-down-osteoarthritis/",
    "https://acespremortho.com/blog/arthoscopic-surgery/",
    "https://acespremortho.com/blog/what-exactly-is-orthopedics/",
    # --- Categories (5) ---
    "https://acespremortho.com/category/uncategorized/",
    "https://acespremortho.com/category/blog/",
    "https://acespremortho.com/category/services/",
    "https://acespremortho.com/category/spinal-conditions/",
    "https://acespremortho.com/category/specialties/",
]


def url_to_filepath(url: str) -> Path:
    parsed = urlparse(url)
    path = parsed.path.strip("/")
    if not path:
        return OUTPUT_DIR / "index.md"
    return OUTPUT_DIR / f"{path}.md"


def fetch_with_jina(url: str) -> Optional[str]:
    headers = {
        "Authorization": f"Bearer {JINA_API_KEY}",
        "Accept": "text/markdown",
        "X-Return-Format": "markdown",
    }
    try:
        resp = requests.get(f"{JINA_BASE}{url}", headers=headers, timeout=30)
        if resp.status_code == 200:
            return resp.text
        print(f"  HTTP {resp.status_code} for {url}")
        return None
    except requests.RequestException as e:
        print(f"  Error fetching {url}: {e}")
        return None


def main():
    total = len(URLS)
    success = 0
    failed = []

    for i, url in enumerate(URLS, 1):
        filepath = url_to_filepath(url)
        filepath.parent.mkdir(parents=True, exist_ok=True)

        print(f"[{i}/{total}] {url}")

        if filepath.exists() and filepath.stat().st_size > 100:
            print(f"  Already exists, skipping")
            success += 1
            continue

        content = fetch_with_jina(url)
        if content:
            source_header = f"---\nsource_url: {url}\nscraped_at: {time.strftime('%Y-%m-%d')}\n---\n\n"
            filepath.write_text(source_header + content, encoding="utf-8")
            size_kb = filepath.stat().st_size / 1024
            print(f"  Saved → {filepath.relative_to(OUTPUT_DIR)} ({size_kb:.1f} KB)")
            success += 1
        else:
            failed.append(url)
            print(f"  FAILED")

        if i < total:
            time.sleep(0.5)

    print(f"\nDone: {success}/{total} succeeded, {len(failed)} failed")
    if failed:
        print("Failed URLs:")
        for u in failed:
            print(f"  - {u}")


if __name__ == "__main__":
    main()
