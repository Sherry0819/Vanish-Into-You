// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * Vanish Into You — LegacyRegistry (skeleton)
 *
 * Stores pointers to encrypted legacy bundles (off-chain) and releases access when called by InheritanceVault.
 * - The bundle itself should be encrypted and stored off-chain (IPFS/Arweave/cloud).
 * - On-chain stores: CID, hash, and encrypted symmetric key per beneficiary.
 *
 * NOTE: In this skeleton we model a single bundle per subject for clarity.
 */

contract LegacyRegistry {
    event BundleRegistered(address indexed subject, string cid, bytes32 contentHash);
    event AccessReleased(address indexed subject, address indexed beneficiary, bytes encryptedKey);

    address public vault; // authorized caller

    modifier onlyVault() {
        require(msg.sender == vault, "not vault");
        _;
    }

    constructor(address _vault) {
        vault = _vault;
    }

    struct Bundle {
        string cid;          // e.g., IPFS CID
        bytes32 contentHash; // hash of encrypted bundle file
        bool exists;
    }

    mapping(address => Bundle) public bundles;
    mapping(address => mapping(address => bytes)) public encryptedKeys; // subject => beneficiary => EncK

    function registerBundle(
        address subject,
        string calldata cid,
        bytes32 contentHash,
        address[] calldata beneficiaries,
        bytes[] calldata encKeys
    ) external {
        require(beneficiaries.length == encKeys.length, "len mismatch");

        bundles[subject] = Bundle({cid: cid, contentHash: contentHash, exists: true});

        for (uint256 i = 0; i < beneficiaries.length; i++) {
            encryptedKeys[subject][beneficiaries[i]] = encKeys[i];
        }

        emit BundleRegistered(subject, cid, contentHash);
    }

    /// Called by vault after inheritance execution to emit AccessReleased events.
    function releaseAccess(address subject, address[] calldata beneficiaries) external onlyVault {
        require(bundles[subject].exists, "no bundle");
        for (uint256 i = 0; i < beneficiaries.length; i++) {
            bytes memory encK = encryptedKeys[subject][beneficiaries[i]];
            emit AccessReleased(subject, beneficiaries[i], encK);
        }
    }
}
